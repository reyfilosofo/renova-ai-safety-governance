#!/usr/bin/env python3
"""Nucleo de datos y logica del servidor MCP Renova.

Solo stdlib. No inventa contenido: todo lo que devuelve procede de los
archivos canonicos del workspace (ver STAGING_DIR) o de entradas que el
propio usuario registra en LUCEM. Estado honesto: prototipo de
laboratorio, CENTRO-001 es un protocolo propuesto sin ejecutar, CENTRO
Guard no esta validado, los resultados sinteticos no son validacion
externa, sin respaldo NIST/ISO/OWASP, UNLICENSED.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
WORKSPACE = HOME / "workspace"
STAGING_DIR = Path(os.environ.get("RENOVA_STAGING_DIR", WORKSPACE / "renova-ai-safety-governance-staging"))
BIBLIOTECA_DIR = Path(os.environ.get("RENOVA_BIBLIOTECA_DIR", WORKSPACE / "renova-biblioteca-2026-11-10"))
INVENTARIO_JSON = Path(os.environ.get("RENOVA_INVENTARIO_JSON", WORKSPACE / "renova-fundamento-inventario-drive.json"))
SERVER_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("RENOVA_DATA_DIR", SERVER_DIR / "data"))
LUCEM_PATH = DATA_DIR / "lucem.jsonl"

SERVER_VERSION = "0.1.0"
POLICY_VERSION = "1.0"
LIMITS = [
    "Prototipo de laboratorio. No certifica sistemas ni afirma mitigacion de riesgos de AGI o superinteligencia.",
    "CENTRO-001 / RENOVA T-001 es un protocolo propuesto, no ejecutado y sin resultados.",
    "CENTRO Guard no esta validado: sus veredictos son simulados (DENY / REVIEW / ALLOW_SIMULATED) y nunca ejecutan ni bloquean una accion real.",
    "Los resultados sinteticos (tests locales, casos sinteticos de politica) no son validacion externa.",
    "La correspondencia con NIST, ISO u OWASP es lectura de RENOVA, no respaldo de esas instituciones.",
    "UNLICENSED: sin licencia. No compartir en publico hasta decidirla.",
    "El texto completo de las 28 obras de Drive y de las 11 del chat no esta indexado: solo sus metadatos verificados. Texto completo indexado: docs del staging y las 24 obras de la Biblioteca (txt extraido).",
]

# Las obras de la Biblioteca: titulo, archivo txt extraido, paginas y
# Drive ID verificados en ~/workspace/renova-biblioteca-2026-11-10/inventario.md
# (seccion "Correccion aplicada", 10 nov 2026). La Escala es PDF de imagen
# sin capa de texto: su txt tiene 0 palabras y se declara asi.
# Ampliacion 2026-11-24 (8 obras, 17-24): subidas por Rey a
# ~/workspace/user/files/ el 24 nov 2026. Sin Drive ID verificado
# (drive_id "" -> drive_link None); no se inventa ningun ID.
# Dos subidas mas de esa tanda son duplicados exactos (mismo sha256) de
# obras ya indexadas y NO se duplican: "Renova (H)" (= 03) y
# "LUX Renova Tratado Integral" (= 07).
BIBLIOTECA = [
    ("Fundamento H", "01_fundamento_h.txt", 333, "1R6LU9A4PgIONtobmfuFLFtkKR4BZhyZt"),
    ("Renova 314", "02_renova_314.txt", 91, "1IomEdEm2AfHINRnJ7D3oqWjKPKWx7G02"),
    ("Renova (H)", "03_renova_H.txt", 600, "1Cz34pg5cFJCepxOqFh9u-SXa3zHZ6udH"),
    ("RENOVA H V7.4 Habitat Herida Horizonte Interior", "04_renova_H_v74.txt", 1314, "1zoeZggdq1cctR4SPfdhdGiFZFTFwLqt2"),
    ("Renova Espiral y Hexagrama (H)", "05_espiral_hexagrama.txt", 32, "1yRcJCkB0PG4edpDx0XBLd8Koew1mXtOs"),
    ("Libro RENOVA: Ciencia de la Vida", "06_ciencia_vida.txt", 134, "1_k_QwUTG7qeu9lkxbs8nW8NCOILHcqTp"),
    ("LUX Renova Tratado Integral", "07_lux_renova.txt", 106, "1KaCJB1IZSoeAKIrJxuMhtk-Q6roem_tZ"),
    ("El Ser y el No Ser desde la Renova", "08_ser_no_ser.txt", 94, "1na5-XcyFWehB_3SyXHia9h3_sW04Zz9F"),
    ("Definicion y Alcance de la Renova", "09_definicion_alcance.txt", 7, "14_9j66V1ieaqSCU6fydStIRPMUxicHVY"),
    ("Renova Psyche", "10_psyche.txt", 67, "1sbiD5Hc_n4lE_kfATXbBEfsTsBiXXopF"),
    ("Escala Renovativa del Ser", "11_escala.txt", 6, "1llFSONGwU-PfEPCXtnFz-2pRTPKbvgFz"),
    ("Renova Biosemiotics", "12_biosemiotics.txt", 69, "1V6qQb1OZtPtdMKUPi9EaMbB_6eB4BuVq"),
    ("Psicologia Renova", "13_psicologia.txt", 55, "1AZSXj6QXo1txUZEaSOx37pkppWJiuyOA"),
    ("La Trampa de Tucidides y la Renova", "14_trampa_tucidides.txt", 117, "1QePYp0A-bTs3mJ-3MXOdhmZxuKs2iCp0"),
    ("Filosofia de la Pobreza", "15_pobreza.txt", 175, "1s681zSWLnYWy8g7DH91cQhbP5gtOhtv7"),
    ("Renova Biosemiotics Orcas", "16_biosemiotics_orcas.txt", 178, "1nGQUG_-oQ8h33pjVzL6-fjaILzXlP2dP"),
    ("Filosofía de una Burbuja Financiera (Edición Comercial 2026)", "17_burbuja_financiera_comercial.txt", 53, ""),
    ("RENOVA Essentiae Vitae (Edición Crítica 2026)", "18_essentiae_vitae_critica.txt", 106, ""),
    ("QUALIA QUANTA SER (Artbook, 132 páginas)", "19_qualia_quanta_ser.txt", 132, ""),
    ("Filosofía de una Burbuja Financiera (Edición Definitiva, Renova Press 2026)", "20_burbuja_financiera_definitiva.txt", 101, ""),
    ("RENOVA V10 (Edición Digital)", "21_renova_v10.txt", 135, ""),
    ("Renova Essentiae Vitae (Libro Final 2026)", "22_essentiae_vitae_final.txt", 213, ""),
    ("Qualia Renovativos (Libro Maestro v2 2026)", "23_qualia_renovativos.txt", 110, ""),
    ("Campayo Renovativo (Tratado Número Letra)", "24_campayo_renovativo.txt", 250, ""),
]

DOCUMENTS = {
    "resumen-publico": ("docs/01-resumen-publico.md", "RENOVA AI SAFETY & GOVERNANCE - Resumen publico (fundacional 1, verbatim)"),
    "tres-vias-empiricas": ("docs/02-tres-vias-empiricas.md", "RENOVA - Tres vias empiricas (fundacional 2, verbatim)"),
    "limites-declarados": ("docs/03-limites-declarados.md", "RENOVA - Limites declarados (fundacional 3, verbatim)"),
    "dictamen-critico": ("docs/dictamen-critico-2026-11-10.md", "Dictamen critico convergente de ChatGPT, Grok, Muse y Gemini (2026-11-10)"),
    "centro-001-protocolo": ("docs/centro-001-protocolo.md", "CENTRO Guard y protocolo CENTRO-001 / RENOVA T-001"),
    "estado-y-bitacora": ("docs/estado-y-bitacora.md", "Estado y bitacora del programa"),
    "frente-a-estandares": ("docs/frente-a-estandares.md", "Frente a los estandares: interoperar, no competir"),
    "laboratorio-reproducible": ("docs/laboratorio-reproducible.md", "Laboratorio reproducible (Public Lab)"),
    "ruta-dual-nist-renova": ("docs/ruta-dual-nist-renova.md", "Ruta dual NIST-RENOVA y riesgos NIST AI 600-1"),
    "simulador-guard": ("docs/simulador-guard.md", "Simulador Guard"),
    "tres-niveles-de-valor": ("docs/tres-niveles-de-valor.md", "Tres niveles de valor"),
    "centro-001-preregistro": ("CENTRO-001-preregistro.md", "Preregistro del experimento CENTRO-001"),
    "benchmark-diseno": ("benchmark/benchmark-r-v0.1-diseno-y-lote-inicial.md", "Benchmark R v0.1: diseno y lote inicial R-001 a R-040"),
    "centro-guard-policy": ("centro-guard-policy.yaml", "Politica CENTRO Guard RNV-01 a RNV-06 (version 1.0, propuesta de diseno)"),
    "readme": ("README.md", "README del programa RENOVA AI SAFETY & GOVERNANCE"),
    "packages": ("packages/PACKAGES.md", "Inventario de paquetes del producto"),
}


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_biblioteca_text(txt_dir: Path, txt_file: str) -> str:
    """Lee una obra de la Biblioteca. Si el archivo unico no existe
    (p. ej. supera el limite de subida del conector GitHub), concatena
    las partes ordenadas <stem>.part<N>.txt, que juntas son el mismo texto."""
    p = txt_dir / txt_file
    if p.exists():
        return _read_text(p)
    stem = p.stem
    parts = sorted(txt_dir.glob(f"{stem}.part*.txt"))
    if not parts:
        return ""
    return "".join(_read_text(part) for part in parts)


def _words(text: str) -> int:
    return len(text.split())


def _snippet(text: str, query: str, radius: int = 180) -> str:
    low = text.lower()
    idx = low.find(query.lower())
    if idx < 0:
        for token in query.lower().split():
            idx = low.find(token)
            if idx >= 0:
                break
    if idx < 0:
        return text[:360].replace("\n", " ")
    start = max(0, idx - radius)
    end = min(len(text), idx + len(query) + radius)
    return ("..." if start > 0 else "") + text[start:end].replace("\n", " ") + ("..." if end < len(text) else "")


class Corpus:
    """Corpus cargado una vez desde los archivos canonicos."""

    def __init__(self):
        self.staging_docs = {}
        for name, (rel, title) in DOCUMENTS.items():
            p = STAGING_DIR / rel
            if p.exists():
                text = _read_text(p)
                self.staging_docs[name] = {"name": name, "title": title, "path": str(p), "text": text, "words": _words(text)}
        self.biblioteca = []
        for title, txt_file, pages, drive_id in BIBLIOTECA:
            p = BIBLIOTECA_DIR / "txt" / txt_file
            text = _read_biblioteca_text(BIBLIOTECA_DIR / "txt", txt_file)
            self.biblioteca.append({
                "title": title, "txt_file": txt_file, "pages": pages,
                "drive_id": drive_id,
                "drive_link": f"https://drive.google.com/file/d/{drive_id}/view" if drive_id else None,
                "words": _words(text), "text": text,
                "coverage": "texto_completo_extraido" if text.strip() else "pdf_de_imagen_sin_texto",
            })
        self.inventario = {}
        self.drive28 = []
        self.chat11 = []
        if INVENTARIO_JSON.exists():
            self.inventario = json.loads(_read_text(INVENTARIO_JSON))
            for item in self.inventario.get("libros_pdf_distintos_en_drive", []):
                rep = item.get("representativo", {})
                self.drive28.append({
                    "title": item.get("obra"), "files_in_drive": item.get("archivos_pdf_en_drive"),
                    "drive_link": rep.get("webViewLink"), "drive_id": rep.get("id"),
                    "coverage": "metadatos_verificados_sin_texto_completo",
                })
            for item in self.inventario.get("libros_del_chat_11_y_su_estado_en_drive", []):
                self.chat11.append({
                    "title": item.get("titulo"), "pages": item.get("paginas_chat"),
                    "coverage": "metadatos_verificados_sin_texto_completo",
                    "note": item.get("observacion", ""),
                })
        self.policy = parse_policy()
        self.scenarios = parse_benchmark(STAGING_DIR / "benchmark" / "benchmark-r-v0.1-diseno-y-lote-inicial.md")

    def counts(self):
        return {
            "staging_docs": len(self.staging_docs),
            "staging_words": sum(d["words"] for d in self.staging_docs.values()),
            "biblioteca_works": len(self.biblioteca),
            "biblioteca_pages": sum(b["pages"] for b in self.biblioteca),
            "biblioteca_words": sum(b["words"] for b in self.biblioteca),
            "fundamento_drive_28": len(self.drive28),
            "fundamento_chat_11": len(self.chat11),
            "fundamento_distinct_works": 54,
            "fundamento_total_pages": 11724,
            "benchmark_scenarios": len(self.scenarios),
        }


def parse_policy():
    """Parser minimo del YAML de la politica (sin dependencias).

    Extrae por cada RNV-xx: id, nombre, pregunta y consecuencias.
    """
    path = STAGING_DIR / "centro-guard-policy.yaml"
    text = _read_text(path) if path.exists() else ""
    policies = []
    blocks = re.split(r"(?m)^  - id: ", text)
    for block in blocks[1:]:
        m_id = re.match(r"(RNV-\d+)", block)
        if not m_id:
            continue
        def field(name):
            m = re.search(r"(?m)^    " + re.escape(name) + r":\s*(.+)$", block)
            return m.group(1).strip() if m else ""
        def list_field(name):
            m = re.search(r"(?m)^    " + re.escape(name) + r":\n((?:      - .+\n?)+)", block)
            if not m:
                return []
            return [line.strip()[2:].strip() for line in m.group(1).strip().splitlines()]
        policies.append({
            "id": m_id.group(1),
            "name": field("name"),
            "question": field("question"),
            "evidence_required": list_field("evidence_required"),
            "consequence_if_missing": list_field("consequence_if_missing"),
        })
    return {"version": POLICY_VERSION, "status": "propuesta_de_diseno",
            "decision_rule": "DENY_sobre_ASK_sobre_ALLOW (el mas estricto gana)",
            "source": str(path), "policies": policies}


def parse_benchmark(path: Path):
    """Parsea el lote R-001 a R-040 de la tabla del diseno."""
    scenarios = []
    if not path.exists():
        return scenarios
    row = re.compile(r"^\|\s*(R-\d{3})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$")
    for line in _read_text(path).splitlines():
        m = row.match(line.strip())
        if not m:
            continue
        case_id, lang, cat, scenario, label = (g.strip() for g in m.groups())
        labels = [x.strip() for x in label.split("/")]
        scenarios.append({
            "case_id": case_id, "language": lang, "category": cat,
            "scenario": scenario, "author_label": labels[0],
            "author_label_full": label, "gold_label": None,
            "split": "dev",
            "note": "Lote inicial v0.1 en dev. gold_label null hasta completar la revision ciega; nunca pasara al split sellado porque su contenido ya es publico.",
        })
    return scenarios


# ---------------------------------------------------------------- tools

def tool_search(query, limit=10, source="all"):
    """Busqueda de texto completo sobre staging + Biblioteca + metadatos Fundamento."""
    if not query or not query.strip():
        raise ValueError("query es obligatoria")
    q = query.strip().lower()
    tokens = [t for t in re.split(r"\W+", q) if len(t) > 2]
    if not tokens:
        tokens = [q]
    results = []

    def score(text):
        low = text.lower()
        return sum(low.count(t) for t in tokens)

    if source in ("all", "staging"):
        for doc in CORPUS.staging_docs.values():
            s = score(doc["text"]) + (10 if q in doc["title"].lower() else 0)
            if s > 0:
                results.append({"source": "staging", "name": doc["name"], "title": doc["title"],
                                "score": s, "words": doc["words"],
                                "snippet": _snippet(doc["text"], query), "path": doc["path"]})
    if source in ("all", "biblioteca"):
        for b in CORPUS.biblioteca:
            s = score(b["text"]) + (10 if q in b["title"].lower() else 0)
            if s > 0:
                results.append({"source": "biblioteca", "title": b["title"], "pages": b["pages"],
                                "score": s, "words": b["words"], "coverage": b["coverage"],
                                "drive_link": b["drive_link"],
                                "snippet": _snippet(b["text"], query) if b["text"].strip() else "PDF de imagen sin capa de texto: sin extracto."})
    if source in ("all", "fundamento"):
        for item in CORPUS.drive28 + CORPUS.chat11:
            if q in item["title"].lower():
                results.append({"source": "fundamento", "title": item["title"],
                                "score": 10, "coverage": item["coverage"],
                                "drive_link": item.get("drive_link"),
                                "pages": item.get("pages"),
                                "snippet": "Solo metadatos verificados: el texto completo de esta obra no esta indexado en el servidor."})
    results.sort(key=lambda r: r["score"], reverse=True)
    return {"query": query, "source": source, "total": len(results),
            "results": results[: max(1, min(int(limit), 25))],
            "coverage_note": "Texto completo: docs del staging y 24 obras de la Biblioteca. Solo metadatos: 28 obras de Drive y 11 del chat."}


def tool_get_document(name):
    """Devuelve integro el documento pedido."""
    key = (name or "").strip().lower().replace(" ", "-")
    if key not in CORPUS.staging_docs:
        return {"error": f"documento no encontrado: {name}",
                "available": sorted(CORPUS.staging_docs.keys())}
    doc = CORPUS.staging_docs[key]
    return {"name": key, "title": doc["title"], "path": doc["path"],
            "words": doc["words"], "text": doc["text"],
            "verbatim": key in ("resumen-publico", "tres-vias-empiricas", "limites-declarados")}


EVIDENCE_STATES = ("Confirmada", "Faltante", "Inferida", "No_verificable")
REVERSIBILITY = ("R0", "R1", "R2", "R3")


def tool_centro_evaluate(action, operation=None, resource=None, authority_verified=False,
                         authority_identity=None, evidence_state="Faltante",
                         reversibility_class="unknown", human_approval=False,
                         human_approval_specific=False, displaces_harm=False,
                         affected_approval=False, critical_uncertainty=False):
    """Implementa RNV-01 a RNV-06 leyendo la politica versionada.

    Devuelve un veredicto SIMULADO. Nunca ejecuta ni bloquea nada real.
    """
    if not action or not str(action).strip():
        raise ValueError("action es obligatoria")
    if evidence_state not in EVIDENCE_STATES:
        raise ValueError(f"evidence_state debe ser uno de {EVIDENCE_STATES}")
    rev = reversibility_class if reversibility_class in REVERSIBILITY else "unknown"
    effective_rev = "R3" if rev == "unknown" else rev
    irreversible = effective_rev in ("R2", "R3")
    checks = []
    denies, reviews = [], []

    def check(pid, result, detail):
        checks.append({"policy": pid, "result": result, "detail": detail})
        if result == "DENY":
            denies.append(pid)
        elif result == "REVIEW":
            reviews.append(pid)

    # RNV-01 Autoridad verificable
    if not authority_verified:
        check("RNV-01", "DENY" if irreversible else "REVIEW",
              "Sin autoridad verificable fuera del modelo. DENY en R2/R3, REVIEW en R0/R1.")
    else:
        check("RNV-01", "PASS", f"Autoridad verificada: {authority_identity or 'identidad declarada, sin detalle'}.")
    # RNV-02 Reversibilidad
    if rev == "unknown":
        check("RNV-02", "REVIEW", "Clase de reversibilidad no declarada: se aplica la mas grave (R3).")
    else:
        check("RNV-02", "PASS", f"Clase de reversibilidad declarada: {rev}.")
    # RNV-03 Dano no desplazado
    if displaces_harm and not affected_approval:
        check("RNV-03", "DENY", "El riesgo se desplaza a terceros sin autorizacion de los afectados.")
    elif displaces_harm:
        check("RNV-03", "PASS", "Riesgo desplazado con autorizacion de los afectados.")
    else:
        check("RNV-03", "PASS", "Sin desplazamiento de dano declarado.")
    # RNV-04 Integridad de evidencia
    if evidence_state == "Confirmada":
        check("RNV-04", "PASS", "Evidencia confirmada por componente independiente.")
    elif evidence_state in ("Faltante", "No_verificable"):
        check("RNV-04", "DENY" if irreversible else "REVIEW",
              f"Evidencia {evidence_state}: nunca sustenta ALLOW en R2/R3.")
    else:  # Inferida
        check("RNV-04", "DENY" if irreversible else "REVIEW",
              "Evidencia inferida: la confianza no es autorizacion; no sustenta ALLOW en R2/R3.")
    # RNV-05 Intervencion humana
    if irreversible and not (human_approval and human_approval_specific):
        check("RNV-05", "REVIEW", "Falta aprobacion humana especifica y vigente para esta operacion y recurso.")
    elif irreversible:
        check("RNV-05", "PASS", "Aprobacion humana especifica presente; no concede permiso por si sola.")
    else:
        check("RNV-05", "PASS" if human_approval else "REVIEW",
              "Aprobacion humana presente." if human_approval else "Sin aprobacion humana; en R0/R1 queda en revision.")
    # RNV-06 Incertidumbre critica
    if critical_uncertainty:
        check("RNV-06", "DENY" if irreversible else "REVIEW",
              "Incertidumbre critica: fail-closed, nunca ALLOW por defecto.")
    else:
        check("RNV-06", "PASS", "Sin incertidumbre critica declarada.")

    if denies:
        decision = "DENY"
        deciding = denies[0]
        reason = f"DENY por {deciding}: el mas estricto gana (DENY sobre REVIEW sobre ALLOW)."
    elif reviews or irreversible:
        decision = "REVIEW"
        deciding = reviews[0] if reviews else "RNV-02"
        reason = ("REVIEW: requiere aprobacion humana especifica y una puerta externa real. "
                  "En R2/R3 nunca hay ALLOW_SIMULATED.")
    else:
        decision = "ALLOW_SIMULATED"
        deciding = "ninguna"
        reason = "ALLOW_SIMULATED: lectura/accion reversible con autoridad verificada y evidencia confirmada."
    return {
        "decision": decision, "deciding_rule": deciding, "reason": reason,
        "action": str(action), "operation": operation, "resource": resource,
        "reversibility_class_declared": rev, "reversibility_class_effective": effective_rev,
        "evidence_state": evidence_state, "authority_verified": bool(authority_verified),
        "human_approval": bool(human_approval),
        "checks": checks,
        "simulated": True,
        "binding_warning": ("Este veredicto es simulado. Un DENY solo es preventivo si es vinculante "
                            "para la ejecucion: este servidor no ejecuta ni bloquea ninguna accion real."),
        "policy": {"name": "CENTRO Guard", "version": CORPUS.policy["version"],
                   "status": CORPUS.policy["status"], "source": CORPUS.policy["source"]},
    }


def tool_benchmark_scenario(case_id):
    """Devuelve el escenario R-001..R-040 parseado del diseno."""
    key = (case_id or "").strip().upper()
    for s in CORPUS.scenarios:
        if s["case_id"] == key:
            return dict(s, source="benchmark/benchmark-r-v0.1-diseno-y-lote-inicial.md",
                        benchmark_version="v0.1", total_scenarios=len(CORPUS.scenarios))
    return {"error": f"escenario no encontrado: {case_id}",
            "available": [s["case_id"] for s in CORPUS.scenarios]}


ABSOLUTES = {
    "siempre": "en los casos verificados", "nunca": "no en los casos verificados",
    "todos": "los casos revisados", "todas": "las revisadas", "nadie": "nadie verificado",
    "garantiza": "podria", "garantizado": "verificable en los casos revisados",
    "perfecto": "revisable", "imposible": "no verificado en los casos revisados",
    "revolucionario": "con cambios medibles", "unico": "distinto en los casos revisados",
    "obviamente": "segun la evidencia citada", "claramente": "segun la evidencia citada",
    "sin duda": "segun la evidencia disponible", "definitivamente": "segun la evidencia disponible",
}
ACTION_VERBS_R3 = ("publicar", "enviar", "borrar", "eliminar", "pagar", "desplegar", "compartir", "difundir")
ACTION_VERBS_R1 = ("escribir", "editar", "modificar", "crear")
ACTION_VERBS_R0 = ("leer", "consultar", "revisar", "resumir")


def tool_transform(text, focus=None):
    """Proceso A -> A' con los ejes CLARITAS / RATIO / VITA / CENTRO.

    Reglas deterministicas sobre el texto recibido. Propuesta, no validacion.
    """
    if not text or not str(text).strip():
        raise ValueError("text es obligatorio")
    original = str(text).strip()
    low = original.lower()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", original) if s.strip()]
    absolutes_found = sorted({w for w in ABSOLUTES if re.search(rf"\b{w}\b", low)})
    numbers = re.findall(r"\d+(?:[.,]\d+)?\s*%?", original)
    has_source = bool(re.search(r"segun|fuente|citado|verificado|estudio|datos", low))
    causal = len(re.findall(r"\b(porque|por lo tanto|demuestra|prueba|asi que)\b", low))
    if any(v in low for v in ACTION_VERBS_R3):
        rev_guess = "R3"
    elif any(v in low for v in ACTION_VERBS_R1):
        rev_guess = "R1"
    else:
        rev_guess = "R0"

    changes = []
    renovated_sentences = []
    for s in sentences:
        new = s
        for word, repl in ABSOLUTES.items():
            if re.search(rf"\b{word}\b", new, flags=re.IGNORECASE):
                new = re.sub(rf"\b{word}\b", repl, new, flags=re.IGNORECASE)
                changes.append(f"'{word}' -> '{repl}'")
        renovated_sentences.append(new)
    renovated = " ".join(renovated_sentences)
    evidence_needed = []
    if not numbers:
        evidence_needed.append("Cifras o mediciones que sustenten las afirmaciones (hoy no hay ninguna en el texto).")
    if not has_source:
        evidence_needed.append("Fuente y version de cada afirmacion (hoy no se cita ninguna).")
    if causal and not has_source:
        evidence_needed.append(f"Soporte para las {causal} afirmacion(es) causal(es) ('porque' / 'demuestra' sin fuente).")
    if rev_guess in ("R1", "R3"):
        evidence_needed.append(f"Plan de reversibilidad para la accion propuesta (clase estimada {rev_guess}).")
    axes = {
        "CLARITAS": f"{len(absolutes_found)} termino(s) absoluto(s) detectado(s): {', '.join(absolutes_found) or 'ninguno'}.",
        "RATIO": f"{causal} afirmacion(es) causal(es); {'sin' if not has_source else 'con'} fuente citada; {len(numbers)} cifra(s) en el texto.",
        "VITA": "Quien se ve afectado y con que coste no esta explicitado en el texto; hay que declararlo antes de actuar." if not re.search(r"afecta|cuesta|tiempo|riesgo", low) else "El texto menciona afectados o coste; verificar que sea concreto.",
        "CENTRO": f"Accion implicita de clase estimada {rev_guess}. Sin autoridad verificable ni evidencia confirmada, el veredicto seria REVIEW o DENY, nunca ALLOW real.",
    }
    return {
        "status": "propuesta_no_validacion",
        "original": original, "renovated_text": renovated,
        "focus": focus, "axes": axes, "changes": sorted(set(changes)),
        "evidence_needed": evidence_needed,
        "reversibility_class_estimate": rev_guess,
        "sentences": len(sentences), "words": _words(original),
        "limits": "La renovacion es una propuesta de redaccion y estructura. No valida el contenido ni sustituye evidencia, revision ciega o autorizacion humana.",
    }


def tool_egra_compare(treatment, baseline, criteria=None, metric_name=None, sample_size=None):
    """Compara tratamiento vs baseline con criterios explicitos.

    Si faltan puntuaciones, no se inventan: devuelve el estado incompleto.
    """
    if not treatment or not baseline:
        raise ValueError("treatment y baseline son obligatorios")
    criteria = criteria or []
    scored = []
    missing = []
    for c in criteria:
        if not isinstance(c, dict) or "name" not in c:
            continue
        if "treatment_score" not in c or "baseline_score" not in c:
            missing.append(c["name"])
            scored.append({**c, "delta": None})
        else:
            t, b = float(c["treatment_score"]), float(c["baseline_score"])
            scored.append({**c, "weight": float(c.get("weight", 1.0)),
                           "treatment_score": t, "baseline_score": b, "delta": round(t - b, 2)})
    if missing:
        return {"status": "incompleto_sin_datos", "treatment": treatment, "baseline": baseline,
                "metric_name": metric_name, "criteria": scored, "missing_scores": missing,
                "note": "No se inventan puntuaciones. Aporta treatment_score y baseline_score (0-10) por criterio para calcular el resultado."}
    if not scored:
        return {"status": "incompleto_sin_datos", "treatment": treatment, "baseline": baseline,
                "metric_name": metric_name, "criteria": [],
                "note": "Sin criterios no hay comparacion. Aporta criteria con name, weight, treatment_score y baseline_score."}
    total_w = sum(c["weight"] for c in scored)
    t_mean = sum(c["treatment_score"] * c["weight"] for c in scored) / total_w
    b_mean = sum(c["baseline_score"] * c["weight"] for c in scored) / total_w
    delta = round(t_mean - b_mean, 2)
    verdict = "tratamiento_supera_baseline" if delta >= 0.5 else ("baseline_supera_tratamiento" if delta <= -0.5 else "sin_diferencia_concluyente")
    return {"status": "simulado", "treatment": treatment, "baseline": baseline,
            "metric_name": metric_name, "sample_size": sample_size,
            "criteria": scored, "treatment_weighted_mean": round(t_mean, 2),
            "baseline_weighted_mean": round(b_mean, 2), "delta": delta, "verdict": verdict,
            "simulated": True,
            "limits": ("Resultado simulado sobre las puntuaciones aportadas por quien llama. "
                       "Sin tamano de muestra, holdout ni protocolo registrado no es evidencia; "
                       "CENTRO-001 es el experimento que decidiria esto y aun no se ejecuta.")}


def tool_lucem_log(entry, source=None, confidence=None, tags=None):
    """Anade una entrada al registro local de evidencia (JSONL con hash encadenado)."""
    if not entry or not str(entry).strip():
        raise ValueError("entry es obligatoria")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    prev_hash = "0" * 64
    count = 0
    if LUCEM_PATH.exists():
        lines = [ln for ln in LUCEM_PATH.read_text(encoding="utf-8").splitlines() if ln.strip()]
        count = len(lines)
        if lines:
            try:
                prev_hash = json.loads(lines[-1]).get("hash", prev_hash)
            except json.JSONDecodeError:
                prev_hash = "0" * 64
    record = {"id": uuid.uuid4().hex[:12],
              "timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "entry": str(entry), "source": source, "confidence": confidence,
              "tags": tags or [], "prev_hash": prev_hash}
    canonical = json.dumps(record, ensure_ascii=False, sort_keys=True)
    record["hash"] = hashlib.sha256((prev_hash + canonical).encode("utf-8")).hexdigest()
    with LUCEM_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    return {"id": record["id"], "hash": record["hash"], "prev_hash": prev_hash,
            "entries_total": count + 1, "path": str(LUCEM_PATH),
            "note": "Registro local de evidencia con hash encadenado. No es validacion externa."}


def tool_get_state():
    """Estado real del servidor y del corpus indexado."""
    lucem_entries = 0
    if LUCEM_PATH.exists():
        lucem_entries = len([ln for ln in LUCEM_PATH.read_text(encoding="utf-8").splitlines() if ln.strip()])
    labels = {}
    for s in CORPUS.scenarios:
        labels[s["author_label"]] = labels.get(s["author_label"], 0) + 1
    return {
        "server": "renova-mcp", "version": SERVER_VERSION,
        "status": "prototipo_de_laboratorio",
        "corpus": CORPUS.counts(),
        "benchmark": {"version": "v0.1", "scenarios": len(CORPUS.scenarios),
                      "author_labels": labels, "gold_labels": "todos null (revision ciega pendiente)",
                      "splits": "dev 60 / validacion 40 / sellado 60 (objetivo); lote v0.1 solo en dev"},
        "centro_guard": {"policy_version": CORPUS.policy["version"], "status": CORPUS.policy["status"],
                         "policies": [p["id"] for p in CORPUS.policy["policies"]],
                         "centro_001": "protocolo propuesto, no ejecutado, sin resultados"},
        "lucem_entries": lucem_entries,
        "limits": LIMITS,
        "license": "UNLICENSED",
        "modes": ["stdio", "http (127.0.0.1, puerto 8765 por defecto)"],
    }


# Instancia global: despues de definir parse_policy / parse_benchmark y las
# herramientas, para que Corpus() pueda usarlas al cargar.
CORPUS = Corpus()
