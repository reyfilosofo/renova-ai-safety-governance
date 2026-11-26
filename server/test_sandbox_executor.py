"""Pruebas del ejecutor de sandbox vinculante (CENTRO-001, prototipo).

Stdlib unittest. Ejecutar desde server/:

    python3 -m unittest test_sandbox_executor -v

Cubre lo que pide la tarea:
  (a) un DENY nunca se ejecuta aunque el llamador lo intente directamente;
  (b) un ALLOW se ejecuta y deja su efecto solo dentro del sandbox;
  (c) un REVIEW sin flag no se ejecuta, con flag si;
  (d) todos los intentos quedan registrados en el JSONL;
  (e) nada escribe fuera del directorio temporal del sandbox.
Mas: prueba de vinculacion (bypass_probe), cadena de hashes LUCEM,
procedencia del gate vendado contra el zip original, y cierre/limpieza.
"""

import hashlib
import inspect
import json
import os
import tempfile
import unittest
import zipfile
from pathlib import Path

import sandbox_executor as se
from sandbox_executor import Action, BindingError, SandboxExecutor

ALLOWED = frozenset({"notes/a.txt", "notes/b.txt", "data/x.txt"})


class ExecutorTestCase(unittest.TestCase):
    def setUp(self):
        # parent_dir propio por test: permite probar (e) con exactitud
        # (nada fuera del directorio temporal del sandbox).
        self.parent = tempfile.TemporaryDirectory(prefix="centro-test-parent-")
        self.ex = SandboxExecutor(ALLOWED, parent_dir=self.parent.name)

    def tearDown(self):
        if not self.ex.closed:
            self.ex.close()
        self.parent.cleanup()

    # -- (a) DENY nunca se ejecuta -------------------------------------
    def test_deny_resource_not_in_allowlist_not_executed(self):
        r = self.ex.execute(Action("WRITE", "secreto.txt", content="x"))
        self.assertEqual(r["verdict"], "DENY")
        self.assertFalse(r["executed"])
        self.assertFalse((self.ex.sandbox_root / "secreto.txt").exists())

    def test_deny_not_executed_even_with_human_approval(self):
        # La via de escape mas obvia: aprobar a mano un DENY.
        r = self.ex.execute(Action("WRITE", "secreto.txt", content="x"),
                            human_approval=True)
        self.assertEqual(r["verdict"], "DENY")
        self.assertFalse(r["executed"])
        self.assertFalse((self.ex.sandbox_root / "secreto.txt").exists())

    def test_deny_invalid_identity_not_executed(self):
        ex = SandboxExecutor(ALLOWED, identity_valid=False,
                             parent_dir=self.parent.name)
        try:
            r = ex.execute(Action("READ", "notes/a.txt"))
            self.assertEqual(r["verdict"], "DENY")
            self.assertEqual(r["gate_reason"], "NO_VERIFIED_IDENTITY")
            self.assertFalse(r["executed"])
        finally:
            ex.close()

    def test_deny_direct_effect_call_with_forged_capability(self):
        # El llamador intenta ejecutar sin pasar por el gate, falsificando
        # la capacidad. Debe fallar sin efecto.
        target = self.ex.sandbox_root / "notes" / "a.txt"
        with self.assertRaises(BindingError):
            self.ex._effect_write(object(), target, "pwned")
        with self.assertRaises(BindingError):
            self.ex._effect_write(None, target, "pwned")
        with self.assertRaises(BindingError):
            self.ex._effect_delete(object(), target)
        self.assertFalse(target.exists())

    def test_execute_accepts_no_verdict_parameter(self):
        # No hay parametro por donde inyectar un veredicto falsificado.
        params = inspect.signature(SandboxExecutor.execute).parameters
        self.assertNotIn("verdict", params)
        self.assertNotIn("decision", params)
        self.assertNotIn("allow", params)

    def test_no_public_module_level_effect_function(self):
        # No existe una via publica de efecto a nivel de modulo.
        public = [n for n in dir(se) if not n.startswith("_")]
        for name in ("write_file", "delete_file", "execute_file",
                     "apply_effect", "run_action", "write", "delete"):
            self.assertNotIn(name, public)

    # -- (b) ALLOW se ejecuta, solo dentro del sandbox ------------------
    def test_allow_read_only_executes_inside_sandbox(self):
        # Sembrar con un WRITE aprobado y leerlo con ALLOW_SIMULATED.
        w = self.ex.execute(Action("WRITE", "notes/a.txt", content="hola"),
                            human_approval=True)
        self.assertTrue(w["executed"])
        r = self.ex.execute(Action("READ", "notes/a.txt"))
        self.assertEqual(r["verdict"], "ALLOW_SIMULATED")
        self.assertTrue(r["executed"])
        self.assertEqual(r["effect"]["content"], "hola")
        self.assertEqual(
            (self.ex.sandbox_root / "notes" / "a.txt").read_text(), "hola")

    def test_allow_evaluate_reports_without_changing_state(self):
        self.ex.execute(Action("WRITE", "notes/a.txt", content="abc"),
                        human_approval=True)
        r = self.ex.execute(Action("EVALUATE", "notes/a.txt"))
        self.assertTrue(r["executed"])
        self.assertEqual(r["effect"]["size_bytes"], 3)
        self.assertTrue(r["effect"]["exists"])
        self.assertEqual((self.ex.sandbox_root / "notes" / "a.txt").read_text(),
                         "abc")

    # -- (c) REVIEW sin flag no; con flag si -----------------------------
    def test_review_write_without_flag_not_executed(self):
        r = self.ex.execute(Action("WRITE", "notes/a.txt", content="x"))
        self.assertEqual(r["verdict"], "REVIEW")
        self.assertFalse(r["executed"])
        self.assertFalse((self.ex.sandbox_root / "notes" / "a.txt").exists())

    def test_review_write_with_flag_executes(self):
        r = self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                            human_approval=True)
        self.assertEqual(r["verdict"], "REVIEW")
        self.assertTrue(r["executed"])
        self.assertEqual(
            (self.ex.sandbox_root / "notes" / "a.txt").read_text(), "x")

    def test_review_delete_without_flag_not_executed(self):
        self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                        human_approval=True)
        r = self.ex.execute(Action("DELETE", "notes/a.txt"))
        self.assertEqual(r["verdict"], "REVIEW")
        self.assertFalse(r["executed"])
        self.assertTrue((self.ex.sandbox_root / "notes" / "a.txt").exists())

    def test_review_delete_with_flag_executes(self):
        self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                        human_approval=True)
        r = self.ex.execute(Action("DELETE", "notes/a.txt"),
                            human_approval=True)
        self.assertTrue(r["executed"])
        self.assertFalse((self.ex.sandbox_root / "notes" / "a.txt").exists())

    def test_review_flag_is_per_call_not_sticky(self):
        # La aprobacion vale para UNA llamada; la siguiente REVIEW sin
        # flag vuelve a no ejecutarse.
        self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                        human_approval=True)
        r = self.ex.execute(Action("DELETE", "notes/a.txt"))
        self.assertFalse(r["executed"])

    # -- (d) todos los intentos quedan registrados -----------------------
    def test_all_attempts_logged_in_jsonl(self):
        self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                        human_approval=True)   # REVIEW, ejecutado
        self.ex.execute(Action("WRITE", "notes/a.txt", content="y"))  # REVIEW, no
        self.ex.execute(Action("READ", "notes/a.txt"))                # ALLOW
        self.ex.execute(Action("WRITE", "secreto.txt", content="z"))  # DENY
        self.ex.execute(Action("WRITE", "../escape.txt", content="z"),
                        human_approval=True)                          # REJECTED
        log_path = self.ex.sandbox_root / ".lucem" / "lucem.jsonl"
        lines = [ln for ln in log_path.read_text(encoding="utf-8")
                 .splitlines() if ln.strip()]
        self.assertEqual(len(lines), 5)
        entries = [json.loads(ln) for ln in lines]
        self.assertEqual(
            [e["attempt"]["verdict"] for e in entries],
            ["REVIEW", "REVIEW", "ALLOW_SIMULATED", "DENY", "REJECTED"])
        self.assertEqual(
            [e["attempt"]["executed"] for e in entries],
            [True, False, True, False, False])
        # Mismo sobre que LUCEM (renova_core.tool_lucem_log).
        for e in entries:
            for key in ("id", "timestamp_utc", "entry", "source", "tags",
                        "prev_hash", "hash", "attempt"):
                self.assertIn(key, e)
            self.assertEqual(e["source"], "centro-001-sandbox-executor")

    def test_lucem_hash_chain_verifies(self):
        for i in range(4):
            self.ex.execute(Action("READ", "notes/a.txt"))
        log_path = self.ex.sandbox_root / ".lucem" / "lucem.jsonl"
        entries = [json.loads(ln) for ln in
                   log_path.read_text(encoding="utf-8").splitlines()
                   if ln.strip()]
        prev = "0" * 64
        for e in entries:
            self.assertEqual(e["prev_hash"], prev)
            record = {k: v for k, v in e.items() if k != "hash"}
            canonical = json.dumps(record, ensure_ascii=False, sort_keys=True)
            expected = hashlib.sha256(
                (prev + canonical).encode("utf-8")).hexdigest()
            self.assertEqual(e["hash"], expected)
            prev = e["hash"]
        # La copia en memoria coincide con el archivo.
        self.assertEqual(len(self.ex.read_log()), len(entries))

    def test_log_export_before_close(self):
        self.ex.execute(Action("READ", "notes/a.txt"))
        dest = Path(self.parent.name) / "exported.jsonl"
        self.ex.export_log(dest)
        self.assertTrue(dest.exists())
        self.assertEqual(len(dest.read_text().splitlines()), 1)

    # -- (e) nada escribe fuera del directorio temporal ------------------
    def test_nothing_written_outside_sandbox(self):
        self.ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                        human_approval=True)
        self.ex.execute(Action("READ", "notes/a.txt"))
        self.ex.execute(Action("WRITE", "secreto.txt", content="y"))
        # El parent solo contiene el directorio del sandbox (y nada mas).
        outside = [p for p in Path(self.parent.name).iterdir()]
        self.assertEqual(len(outside), 1)
        self.assertEqual(outside[0], self.ex.sandbox_root)
        # Y dentro del sandbox solo estan los archivos de la accion y .lucem.
        inside = sorted(p.relative_to(self.ex.sandbox_root).as_posix()
                        for p in self.ex.sandbox_root.rglob("*") if p.is_file())
        self.assertEqual(inside, [".lucem/lucem.jsonl", "notes/a.txt"])

    def test_path_traversal_rejected_no_write_outside(self):
        sentinel = Path(self.parent.name) / "escape.txt"
        r = self.ex.execute(Action("WRITE", "../escape.txt", content="x"),
                            human_approval=True)
        self.assertEqual(r["verdict"], "REJECTED")
        self.assertFalse(r["executed"])
        self.assertFalse(sentinel.exists())
        r2 = self.ex.execute(Action("WRITE", "notes/../../escape2.txt",
                                    content="x"), human_approval=True)
        self.assertFalse(r2["executed"])
        self.assertFalse((Path(self.parent.name) / "escape2.txt").exists())

    def test_absolute_path_rejected(self):
        r = self.ex.execute(
            Action("WRITE", "/tmp/centro-absoluto.txt", content="x"),
            human_approval=True)
        self.assertEqual(r["verdict"], "REJECTED")
        self.assertFalse(r["executed"])
        self.assertFalse(Path("/tmp/centro-absoluto.txt").exists())

    def test_evidence_dir_not_writable_by_actions(self):
        r = self.ex.execute(
            Action("WRITE", ".lucem/lucem.jsonl", content="forged"),
            human_approval=True)
        self.assertEqual(r["verdict"], "REJECTED")
        self.assertFalse(r["executed"])
        # El registro sigue intacto: una sola entrada, la del rechazo.
        self.assertEqual(len(self.ex.read_log()), 1)

    def test_symlink_escape_rejected(self):
        outside = Path(self.parent.name) / "victima.txt"
        outside.write_text("original")
        link = self.ex.sandbox_root / "notes" / "enlace.txt"
        link.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(outside, link)
        r = self.ex.execute(
            Action("WRITE", "notes/enlace.txt", content="sobrescrito"),
            human_approval=True)
        self.assertFalse(r["executed"])
        self.assertEqual(outside.read_text(), "original")

    # -- operaciones sin efecto confinado ---------------------------------
    def test_non_file_operations_not_executed_even_when_approved(self):
        # SEND es REVIEW y con aprobacion el gate lo dejaria pasar, pero
        # el sandbox no tiene efecto confinado para enviar nada: no se
        # ejecuta y queda registrado como tal (hueco declarado).
        r = self.ex.execute(Action("SEND", "notes/a.txt"),
                            human_approval=True)
        self.assertEqual(r["verdict"], "REVIEW")
        self.assertFalse(r["executed"])
        self.assertIn("NO_CONFINED_EFFECT_DEFINED", r["execution_reason"])

    # -- prueba de vinculacion (preregistro seccion 6) --------------------
    def test_bypass_probe_all_blocked(self):
        results = self.ex.bypass_probe()
        self.assertTrue(results)
        for item in results:
            self.assertTrue(item["blocked"],
                            f"bypass NOT blocked: {item['route']} "
                            f"({item['detail']})")

    # -- cierre y limpieza -------------------------------------------------
    def test_execute_after_close_raises(self):
        self.ex.close()
        with self.assertRaises(RuntimeError):
            self.ex.execute(Action("READ", "notes/a.txt"))

    def test_close_removes_sandbox_directory(self):
        root = self.ex.sandbox_root
        self.assertTrue(root.exists())
        self.ex.close()
        self.assertFalse(root.exists())
        self.assertTrue(self.ex.closed)

    def test_context_manager_cleans_up(self):
        with SandboxExecutor(ALLOWED, parent_dir=self.parent.name) as ex:
            root = ex.sandbox_root
            ex.execute(Action("WRITE", "notes/a.txt", content="x"),
                       human_approval=True)
            self.assertTrue((root / "notes" / "a.txt").exists())
        self.assertFalse(root.exists())

    # -- validacion de acciones --------------------------------------------
    def test_invalid_operation_rejected_at_construction(self):
        with self.assertRaises(ValueError):
            Action("FLY", "notes/a.txt")

    def test_write_without_content_rejected_at_construction(self):
        with self.assertRaises(ValueError):
            Action("WRITE", "notes/a.txt")

    # -- procedencia del gate vendado ---------------------------------------
    def test_gate_provenance_matches_original_zip(self):
        """El gate vendado es byte-identico al del stack v2.0 original."""
        zip_path = Path(os.path.expanduser(se.GATE_SOURCE_ZIP))
        self.assertTrue(zip_path.exists())
        with zipfile.ZipFile(zip_path) as z:
            names = z.namelist()
            ag = [n for n in names if n.endswith("/04_SOFTWARE/renova_stack/action_gate.py")]
            ct = [n for n in names if n.endswith("/04_SOFTWARE/renova_stack/contracts.py")]
            self.assertEqual(len(ag), 1)
            self.assertEqual(len(ct), 1)
            self.assertEqual(
                hashlib.sha256(z.read(ag[0])).hexdigest(),
                se.GATE_ACTION_GATE_SHA256)
            self.assertEqual(
                hashlib.sha256(z.read(ct[0])).hexdigest(),
                se.GATE_CONTRACTS_SHA256)
            self.assertEqual(
                hashlib.sha256(zip_path.read_bytes()).hexdigest(),
                se.GATE_SOURCE_ZIP_SHA256)


if __name__ == "__main__":
    unittest.main()
