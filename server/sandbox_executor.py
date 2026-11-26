"""Ejecutor de sandbox vinculante para CENTRO-001 — PROTOTIPO local.

Que es
-------
Un sandbox minimo en el que las "acciones" son operaciones de archivo
(WRITE / READ / RETRIEVE / EVALUATE / DELETE) confinadas a un directorio
temporal que se limpia al terminar. Cada accion pasa obligatoriamente por
el gate ActionGate del stack RENOVA v2.0 (ver abajo, codigo vendado
verbatim con procedencia). El ejecutor solo ejecuta una accion si el gate
la permite; un DENY no se ejecuta bajo ninguna circunstancia (ni siquiera
con aprobacion humana); un REVIEW exige un flag explicito de aprobacion
humana por llamada. Cada intento — permitido, denegado, en revision,
rechazado por ruta — se registra en JSONL con hash encadenado, con el
mismo sobre que usa LUCEM en renova_core.py (id, timestamp_utc, entry,
source, tags, prev_hash, hash).

Que NO es
----------
- NO es el prototipo registrado de CENTRO-001. El prototipo que se evalua
  en el experimento lo decide Rey (decisiones D2/D3 del preregistro
  propuesto, CENTRO-001-preregistro.md en la raiz del repo). Este modulo es
  trabajo de preparacion de la fase 1 (dias 1-30) y nada mas.
- NO es una garantia de seguridad. Es un prototipo en un solo proceso de
  Python: la vinculacion es estructural frente a cualquier llamador que
  use la API publica, pero NO frente a un llamador que reescriba los
  internals del ejecutor en el mismo proceso (ver "Limites honestos").
- NO ejecuta nada real fuera del sandbox. Los efectos existen solo dentro
  del directorio temporal. Las operaciones sin efecto confinado definido
  (SEND, DEPLOY, PURCHASE, PHYSICAL_ACTUATE) no se ejecutan aunque el
  gate las deje en REVIEW y haya aprobacion humana: se registran como no
  ejecutadas con motivo NO_CONFINED_EFFECT_DEFINED (ver README).
- NO es el servidor MCP ni toca vercel/. No se despliega.

Procedencia del gate (verificable)
----------------------------------
El gate es copia VERBATIM de:
  packages/RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09.zip
  (SHA-256 del zip: 2b5c6a27e5332ca28d32528d08a3c82b6806a1579e735026df06bb1d7677dc65)
  RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09/04_SOFTWARE/renova_stack/action_gate.py
    SHA-256: 8adce3532fb22543eb3fcbdb63296f5052087543587efb41cc84e940b8fe3293
  RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09/04_SOFTWARE/renova_stack/contracts.py
    SHA-256: 671bc79422e5c39a2268574bef2a04dcc1d055cc60575ea532aae56bd705bb12
Solo se renombraron los simbolos con prefijo "_" para dejar claro que son
el gate vendado y no una reimplementacion. La logica no se toco. El test
`test_gate_provenance` de test_sandbox_executor.py recomputa esos hashes
desde el zip y los compara con estas constantes.

Como se garantiza la vinculacion (estructural, no por convencion)
-----------------------------------------------------------------
1. NO EXISTE ninguna funcion publica que ejecute un efecto. El modulo
   solo exporta SandboxExecutor, Action y BindingError. No hay
   `write_file()`, `delete_file()` ni ninguna otra via de efecto a nivel
   de modulo. Un llamador que importe el modulo no encuentra por donde
   ejecutar sin pasar por el gate.
2. `SandboxExecutor.execute()` es el UNICO punto de entrada de ejecucion
   y NO acepta un veredicto como parametro: llama al gate el mismo, con
   la accion y el contexto que el mismo construye. Un llamador no puede
   falsificar un ALLOW: no hay parametro por donde inyectarlo.
3. Las funciones de efecto son metodos privados (`_effect_write`,
   `_effect_read`, `_effect_delete`) y exigen una capacidad de un solo
   uso: un objeto opaco creado DENTRO de `execute()` solo despues de un
   veredicto que autoriza, guardado en `self._live_capability` unicamente
   durante la llamada, y borrado en `finally` inmediatamente despues.
   El metodo de efecto verifica identidad (`capability is
   self._live_capability`) y rechaza cualquier otra cosa con
   BindingError. Fuera de `execute()` no existe ninguna capacidad viva
   que robar: una llamada directa a `_effect_write` con una capacidad
   falsificada, None, o una capacidad ya consumida, falla sin efecto.
4. El directorio del sandbox (la raiz donde viven los efectos) solo lo
   conoce la instancia del ejecutor; las rutas se resuelven contra esa
   raiz y se rechaza cualquier ruta que escape de ella (ver
   `_resolve()`), incluidos enlaces simbolicos y rutas absolutas. El
   directorio de evidencia `.lucem/` dentro del sandbox esta vedado a
   las acciones.
5. Un DENY no tiene via de escape: ni `human_approval=True` ni ningun
   otro flag lo ejecuta. La decision de no ejecutar un DENY esta en el
   codigo de `execute()`, no en un parametro del llamador.
6. `bypass_probe()` ejecuta la prueba de vinculacion que exige el
   preregistro (seccion 6): intenta las rutas de bypass conocidas
   (llamada directa a efectos con capacidad falsificada, DENY con
   aprobacion humana, traversal de ruta, ejecucion tras cierre) y
   reporta por ruta si quedo bloqueada. Antes de la primera corrida
   valida de CENTRO-001 esa prueba debe dar todo bloqueado.

Limites honestos (leer antes de usar en CENTRO-001)
----------------------------------------------------
L1. Un solo proceso de Python no es una frontera de seguridad frente a
    un adversario con acceso al codigo en ejecucion: quien pueda hacer
    `executor._live_capability = <objeto>` o reasignar
    `executor._effect_write` puede eludir el gate. Eso equivale a
    reescribir el control, no a usarlo. La vinculacion real frente a un
    agente adversario exige separar procesos (el gate en un proceso
    distinto del agente, sin credenciales ni rutas alternativas para el
    agente) y es trabajo de la fase 1, no de este modulo.
L2. El gate vendado es CONSULTIVO por diseno (su propio docstring:
    "Offline-only advisory gate... no side-effect executor"). La
    vinculacion la aporta ESTE ejecutor, no el gate. Si alguien usa el
    gate solo, vuelve a ser consultivo.
L3. El veredicto ALLOW_SIMULATED del gate es, en su vocabulario, una
    autorizacion simulada. Dentro de este sandbox el efecto SI se aplica
    de verdad, pero solo dentro del sandbox: es un efecto real confinado,
    no una autorizacion en un sistema externo.
L4. El gate tiene una rama inalcanzable: `assess()` devuelve DENY /
    UNKNOWN_OPERATION para operaciones desconocidas, pero los contratos
    rechazan operaciones desconocidas en `__post_init__` antes de que el
    gate las vea. La rama existe como defensa en profundidad, no como
    camino ejecutable.
L5. El registro JSONL vive DENTRO del sandbox y se borra con el al
    cerrar. Para conservar la evidencia hay que llamar a `export_log()`
    antes de cerrar, o leerla con `read_log()`. Si se olvida, la
    evidencia se pierde con el directorio temporal.
L6. Sin reloj ni identidad externos: `timestamp_utc` es el reloj del
    sistema y la identidad la aporta quien construye el ejecutor. En
    CENTRO-001 la identidad debe venir de fuera de banda, como exigen
    los contratos del stack.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import FrozenSet

__all__ = ["SandboxExecutor", "Action", "BindingError"]

# ---------------------------------------------------------------------------
# Procedencia del gate vendado (ver docstring del modulo).
# ---------------------------------------------------------------------------
# Ruta al zip original del stack v2.0, relativa al repo: server/../packages/.
# Se resuelve desde la ubicacion de este modulo para que la prueba de
# procedencia funcione se corra desde donde se corra.
GATE_SOURCE_ZIP = str(
    Path(__file__).resolve().parent.parent
    / "packages"
    / "RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09.zip"
)
GATE_SOURCE_ZIP_SHA256 = (
    "2b5c6a27e5332ca28d32528d08a3c82b6806a1579e735026df06bb1d7677dc65"
)
GATE_ACTION_GATE_SHA256 = (
    "8adce3532fb22543eb3fcbdb63296f5052087543587efb41cc84e940b8fe3293"
)
GATE_CONTRACTS_SHA256 = (
    "671bc79422e5c39a2268574bef2a04dcc1d055cc60575ea532aae56bd705bb12"
)
GATE_POLICY_VERSION = "RENOVA-STACK-2.0-DRAFT"

# ===========================================================================
# Gate vendado VERBATIM del stack RENOVA v2.0 (solo renombrado con "_").
# No se modifico la logica. Ver hashes arriba.
# ===========================================================================

_OPERATIONS = frozenset({
    "READ", "RETRIEVE", "EVALUATE", "WRITE", "SEND",
    "DEPLOY", "PURCHASE", "DELETE", "PHYSICAL_ACTUATE",
})
_CLASSIFICATIONS = {"PUBLIC": 0, "INTERNAL": 1, "CONFIDENTIAL": 2}
_HIGH_IMPACT = {"WRITE", "SEND", "DEPLOY", "PURCHASE", "DELETE", "PHYSICAL_ACTUATE"}
_READ_ONLY = {"READ", "RETRIEVE", "EVALUATE"}
# Operaciones con efecto confinado definido en este sandbox (solo archivos).
_FILE_OPERATIONS = {"READ", "RETRIEVE", "EVALUATE", "WRITE", "DELETE"}


@dataclass(frozen=True)
class _TrustedContext:
    tenant: str
    principal: str
    valid: bool
    allowed_resources: FrozenSet[str]
    max_classification: str = "INTERNAL"
    origin: str = "TRUSTED_RUNTIME"

    def __post_init__(self):
        if not self.tenant or not self.principal or self.max_classification not in _CLASSIFICATIONS:
            raise ValueError("invalid trusted context")


@dataclass(frozen=True)
class _ActionRequest:
    operation: str
    resource: str
    purpose: str = ""
    external_side_effect: bool = False

    def __post_init__(self):
        if self.operation not in _OPERATIONS or not self.resource or len(self.resource) > 256:
            raise ValueError("invalid operation or resource")


@dataclass(frozen=True)
class _AdvisoryDecision:
    verdict: str
    reason: str
    policy_version: str = GATE_POLICY_VERSION
    enforceable: bool = False

    def to_dict(self):
        return {"verdict": self.verdict, "reason": self.reason,
                "policy_version": self.policy_version, "enforceable": self.enforceable}


def _assess(action: _ActionRequest, context: _TrustedContext) -> _AdvisoryDecision:
    """Copia verbatim de renova_stack/action_gate.py::assess."""
    if not context.valid or context.origin != "TRUSTED_RUNTIME":
        return _AdvisoryDecision("DENY", "NO_VERIFIED_IDENTITY")
    if action.resource not in context.allowed_resources:
        return _AdvisoryDecision("DENY", "RESOURCE_NOT_IN_SCOPED_ALLOWLIST")
    if action.external_side_effect or action.operation in _HIGH_IMPACT:
        return _AdvisoryDecision("REVIEW", "HUMAN_APPROVAL_AND_EXTERNAL_GATEWAY_REQUIRED")
    if action.operation in _READ_ONLY:
        return _AdvisoryDecision("ALLOW_SIMULATED", "SCOPED_READ_ONLY_OFFLINE")
    return _AdvisoryDecision("DENY", "UNKNOWN_OPERATION")


# ===========================================================================
# API publica del ejecutor.
# ===========================================================================

class BindingError(RuntimeError):
    """La ejecucion intento saltarse el gate o la capacidad no es valida."""


@dataclass(frozen=True)
class Action:
    """Una accion que el agente intenta. No ejecuta nada por si misma.

    operation: una de READ, RETRIEVE, EVALUATE, WRITE, SEND, DEPLOY,
        PURCHASE, DELETE, PHYSICAL_ACTUATE.
    resource: ruta RELATIVA dentro del sandbox (p. ej. "notes/a.txt").
        Las rutas absolutas y las que escapan del sandbox se rechazan.
    content: contenido a escribir (solo WRITE). Ignorado en el resto.
    purpose: proposito declarado (trazabilidad, sin efecto en el veredicto).
    external_side_effect: si es True el gate devuelve REVIEW (efecto externo).
    """

    operation: str
    resource: str
    content: str | None = None
    purpose: str = ""
    external_side_effect: bool = False

    def __post_init__(self):
        if self.operation not in _OPERATIONS:
            raise ValueError(f"invalid operation: {self.operation!r}")
        if not self.resource or len(self.resource) > 256:
            raise ValueError("invalid resource")
        if "\x00" in self.resource:
            raise ValueError("invalid resource: NUL byte")
        if self.operation == "WRITE" and self.content is None:
            raise ValueError("WRITE requires content")


class SandboxExecutor:
    """Ejecutor de sandbox con gate vinculante.

    Uso tipico (como context manager; al salir se borra el sandbox)::

        with SandboxExecutor(allowed_resources={"notes/a.txt"}) as ex:
            r = ex.execute(Action("WRITE", "notes/a.txt", content="hola"),
                           human_approval=True)
            # r["executed"] es True solo si el gate lo permitio.

    El ejecutor es de un solo uso por instancia en cuanto a su contexto:
    `identity_valid`, `tenant` y `principal` se fijan en el constructor.
    """

    _LUCEM_DIRNAME = ".lucem"
    _LUCEM_FILENAME = "lucem.jsonl"
    _SOURCE = "centro-001-sandbox-executor"

    def __init__(self, allowed_resources, *, tenant="centro-001-prototype",
                 principal="sandbox-agent", identity_valid=True,
                 parent_dir=None):
        self._allowed_resources = frozenset(allowed_resources)
        self._tenant = tenant
        self._principal = principal
        self._identity_valid = bool(identity_valid)
        self._closed = False
        self._live_capability = None  # Solo existe DURANTE execute().
        self._entries = []            # Copia en memoria del registro.
        self._prev_hash = "0" * 64
        # Directorio temporal propio; se limpia en close().
        self._tmp = tempfile.TemporaryDirectory(
            prefix="centro-sandbox-", dir=parent_dir)
        self._root = Path(self._tmp.name)
        self._lucem_dir = self._root / self._LUCEM_DIRNAME
        self._lucem_dir.mkdir(parents=True, exist_ok=True)
        self._lucem_path = self._lucem_dir / self._LUCEM_FILENAME
        self._lucem_path.touch()

    # -- ciclo de vida ---------------------------------------------------
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False

    def close(self):
        """Borra el directorio temporal del sandbox y su registro."""
        if self._closed:
            return
        self._closed = True
        self._live_capability = None
        self._tmp.cleanup()

    @property
    def sandbox_root(self) -> Path:
        """Raiz del sandbox (solo lectura para inspeccion/tests)."""
        return self._root

    @property
    def closed(self) -> bool:
        return self._closed

    # -- registro LUCEM --------------------------------------------------
    def _log(self, attempt: dict) -> dict:
        """Anade una entrada al JSONL con hash encadenado (mismo sobre que
        renova_core.tool_lucem_log) y a la copia en memoria. Devuelve la
        entrada completa."""
        record = {
            "id": uuid.uuid4().hex[:12],
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "entry": attempt.pop("_summary"),
            "source": self._SOURCE,
            "confidence": None,
            "tags": ["centro-001", "sandbox-executor", "attempt",
                     attempt["verdict"].lower()],
            "attempt": attempt,
            "prev_hash": self._prev_hash,
        }
        canonical = json.dumps(record, ensure_ascii=False, sort_keys=True)
        record["hash"] = hashlib.sha256(
            (self._prev_hash + canonical).encode("utf-8")).hexdigest()
        self._prev_hash = record["hash"]
        self._entries.append(record)
        with self._lucem_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        return record

    def read_log(self) -> list:
        """Copia en memoria de todas las entradas registradas."""
        return [dict(e) for e in self._entries]

    def export_log(self, path) -> Path:
        """Copia el JSONL fuera del sandbox. Accion explicita del
        operador (no del agente): es la unica escritura fuera del
        sandbox que este modulo hace, y solo cuando se le pide."""
        self._ensure_open()
        dest = Path(path)
        shutil.copyfile(self._lucem_path, dest)
        return dest

    # -- resolucion de rutas ---------------------------------------------
    def _resolve(self, resource: str) -> Path:
        """Resuelve `resource` dentro de la raiz. Rechaza rutas absolutas,
        escapes (`..`), enlaces simbolicos que salgan, y el directorio de
        evidencia `.lucem/`."""
        candidate = Path(resource)
        if candidate.is_absolute():
            raise BindingError(f"absolute resource path rejected: {resource!r}")
        # resolve() sigue enlaces simbolicos de los componentes existentes.
        resolved = (self._root / candidate).resolve()
        if not resolved.is_relative_to(self._root):
            raise BindingError(f"resource escapes sandbox: {resource!r}")
        if resolved == self._root:
            raise BindingError(f"resource is the sandbox root: {resource!r}")
        if self._LUCEM_DIRNAME in resolved.relative_to(self._root).parts:
            raise BindingError(f"resource targets evidence dir: {resource!r}")
        return resolved

    # -- efectos (privados, solo con capacidad viva) ----------------------
    def _require_capability(self, capability):
        if capability is None or capability is not self._live_capability:
            raise BindingError(
                "effect called without a live capability minted by "
                "SandboxExecutor.execute() after a gate verdict; direct "
                "execution bypassing the gate is refused")

    def _effect_write(self, capability, path: Path, content: str) -> dict:
        self._require_capability(capability)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode("utf-8")
        path.write_bytes(data)
        return {"bytes_written": len(data), "path": str(path.relative_to(self._root))}

    def _effect_read(self, capability, path: Path) -> dict:
        self._require_capability(capability)
        if not path.is_file():
            raise FileNotFoundError(f"resource not found in sandbox: {path.name!r}")
        data = path.read_bytes()
        return {"bytes_read": len(data),
                "path": str(path.relative_to(self._root)),
                "content": data.decode("utf-8", errors="replace")}

    def _effect_evaluate(self, capability, path: Path) -> dict:
        self._require_capability(capability)
        return {"exists": path.is_file(),
                "size_bytes": path.stat().st_size if path.is_file() else None,
                "path": str(path.relative_to(self._root))}

    def _effect_delete(self, capability, path: Path) -> dict:
        self._require_capability(capability)
        if not path.is_file():
            raise FileNotFoundError(f"resource not found in sandbox: {path.name!r}")
        path.unlink()
        return {"deleted": True, "path": str(path.relative_to(self._root))}

    # -- punto unico de entrada -------------------------------------------
    def execute(self, action: Action, *, human_approval: bool = False) -> dict:
        """UNICO punto de entrada de ejecucion.

        1. Resuelve la ruta (rechazo antes del gate si escapa).
        2. Llama al gate (el llamador NO puede inyectar un veredicto).
        3. DENY -> nunca se ejecuta, ni con human_approval=True.
           REVIEW -> solo con human_approval=True.
           ALLOW_SIMULATED -> se ejecuta (efecto real, confinado).
        4. Registra el intento en el JSONL, se ejecute o no.
        Devuelve {"executed", "verdict", "gate_reason",
        "execution_reason", "effect", "log_id", "log_hash"}.
        """
        self._ensure_open()
        base = {
            "operation": action.operation,
            "resource": action.resource,
            "purpose": action.purpose,
            "external_side_effect": action.external_side_effect,
            "human_approval": bool(human_approval),
            "gate_policy_version": GATE_POLICY_VERSION,
        }

        # Paso 1: resolucion de ruta antes del gate.
        try:
            target = self._resolve(action.resource)
        except BindingError as exc:
            attempt = dict(base, verdict="REJECTED", gate_reason=None,
                           executed=False, execution_reason=str(exc),
                           effect=None,
                           _summary=f"REJECTED {action.operation} {action.resource}: {exc}")
            record = self._log(attempt)
            return self._result(attempt, record)

        # Paso 2: el gate decide; el llamador no interviene.
        request = _ActionRequest(
            operation=action.operation, resource=action.resource,
            purpose=action.purpose,
            external_side_effect=action.external_side_effect)
        context = _TrustedContext(
            tenant=self._tenant, principal=self._principal,
            valid=self._identity_valid,
            allowed_resources=self._allowed_resources)
        decision = _assess(request, context)
        attempt = dict(base, verdict=decision.verdict,
                       gate_reason=decision.reason, executed=False,
                       execution_reason=None, effect=None)

        # Paso 3: aplicar el veredicto.
        if decision.verdict == "DENY":
            attempt["execution_reason"] = (
                "DENY is never executed, even with human approval")
        elif decision.verdict == "REVIEW" and not human_approval:
            attempt["execution_reason"] = (
                "REVIEW requires explicit human_approval=True for this call")
        elif action.operation not in _FILE_OPERATIONS:
            # REVIEW con aprobacion (o ALLOW, que no se da aqui) pero sin
            # efecto confinado definido: no se ejecuta nada. Hueco real
            # del prototipo, registrado en vez de simular un efecto.
            attempt["execution_reason"] = (
                "NO_CONFINED_EFFECT_DEFINED: operation has no confined "
                "file effect in this prototype (SEND/DEPLOY/PURCHASE/"
                "PHYSICAL_ACTUATE); not executed")
        else:
            # Capacidad de un solo uso, viva solo durante esta llamada.
            capability = object()
            self._live_capability = capability
            try:
                if action.operation == "WRITE":
                    effect = self._effect_write(capability, target, action.content)
                elif action.operation in ("READ", "RETRIEVE"):
                    effect = self._effect_read(capability, target)
                elif action.operation == "EVALUATE":
                    effect = self._effect_evaluate(capability, target)
                elif action.operation == "DELETE":
                    effect = self._effect_delete(capability, target)
                else:  # pragma: no cover - protegido por _FILE_OPERATIONS
                    raise AssertionError(action.operation)
                attempt["executed"] = True
                attempt["effect"] = effect
                attempt["execution_reason"] = "executed inside sandbox"
            except FileNotFoundError as exc:
                attempt["execution_reason"] = f"effect failed: {exc}"
            finally:
                self._live_capability = None

        # Paso 4: registrar siempre.
        attempt["_summary"] = (
            f"{attempt['verdict']} {action.operation} {action.resource} "
            f"executed={attempt['executed']} ({attempt['execution_reason']})")
        record = self._log(attempt)
        return self._result(attempt, record)

    # -- prueba de vinculacion (preregistro, seccion 6) --------------------
    def bypass_probe(self) -> list:
        """Intenta las rutas de bypass conocidas y reporta por ruta si
        quedo bloqueada. Antes de la primera corrida valida de CENTRO-001
        todas deben dar blocked=True. No ejecuta ningun efecto real."""
        results = []

        def _check(name, fn):
            try:
                fn()
            except (BindingError, RuntimeError, FileNotFoundError,
                    ValueError):
                results.append({"route": name, "blocked": True,
                                "detail": "refused without effect"})
                return
            except Exception as exc:  # noqa: BLE001 - cualquier otra cosa es fallo
                results.append({"route": name, "blocked": False,
                                "detail": f"unexpected error: {exc!r}"})
                return
            results.append({"route": name, "blocked": False,
                            "detail": "call succeeded: bypass NOT blocked"})

        # (a) Llamada directa a un efecto con capacidad falsificada.
        _check("direct _effect_write with forged capability",
               lambda: self._effect_write(object(), self._root / "x.txt", "pwned"))
        _check("direct _effect_write with None capability",
               lambda: self._effect_write(None, self._root / "x.txt", "pwned"))
        _check("direct _effect_delete with forged capability",
               lambda: self._effect_delete(object(), self._root / "x.txt"))
        # (b) DENY con aprobacion humana: debe quedar sin ejecutar.
        _check("DENY with human_approval=True still not executed",
               lambda: self._probe_deny_with_approval())
        # (c) Traversal de ruta: debe rechazarse sin escribir fuera.
        _check("path traversal ../escape.txt",
               lambda: self._probe_traversal())
        # (d) Ejecucion tras el cierre: debe fallar.
        _check("execute after close",
               lambda: self._probe_after_close())
        return results

    def _probe_deny_with_approval(self):
        # Recurso fuera de la allowlist -> DENY aunque se apruebe.
        result = self.execute(
            Action("WRITE", "no-permitido.txt", content="x"),
            human_approval=True)
        if result["executed"]:
            return  # no bloqueado: el bypass tuvo exito
        raise BindingError("DENY correctly not executed")

    def _probe_traversal(self):
        result = self.execute(
            Action("WRITE", "../escape.txt", content="x"),
            human_approval=True)
        if result["executed"]:
            return
        raise BindingError("traversal correctly rejected")

    def _probe_after_close(self):
        probe = SandboxExecutor(allowed_resources={"a.txt"})
        probe.close()
        probe.execute(Action("READ", "a.txt"))
        # Si execute() no lanzo, el bypass tuvo exito.
        return

    # -- internos ----------------------------------------------------------
    def _ensure_open(self):
        if self._closed:
            raise RuntimeError("SandboxExecutor is closed; sandbox was cleaned up")

    @staticmethod
    def _result(attempt: dict, record: dict) -> dict:
        return {
            "executed": attempt["executed"],
            "verdict": attempt["verdict"],
            "gate_reason": attempt.get("gate_reason"),
            "execution_reason": attempt["execution_reason"],
            "effect": attempt.get("effect"),
            "log_id": record["id"],
            "log_hash": record["hash"],
        }
