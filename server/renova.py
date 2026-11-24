#!/usr/bin/env python3
"""CLI / bot Renova: `renovar`.

Uso principal (pipeline A -> A' + CENTRO + LUCEM):
  python3 renova.py "La IA siempre tiene la razon"
  python3 renova.py --file texto.md
  python3 renova.py --file texto.md --out renovado.md
  ./renovar "texto"

Subcomandos: search, document, scenario, state, evaluate, transform,
compare, log. Todos llaman a renova_core.py, el mismo nucleo del
servidor MCP: lo que hace el CLI es lo que hacen las herramientas.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from renova_core import (tool_benchmark_scenario, tool_centro_evaluate,
                         tool_egra_compare, tool_get_document,
                         tool_get_state, tool_lucem_log, tool_search,
                         tool_transform)


def _read_input(args) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.text:
        return " ".join(args.text)
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("renovar necesita un texto o --file. Ejemplo: ./renovar \"La IA siempre tiene la razon\"")


def _md_renovacion(text, transformed, verdict, log):
    lines = ["# Renova: A -> A'", "", "## Texto original", "", text, "",
             "## Texto renovado", "", transformed["renovated_text"], "",
             "## Ejes", ""]
    for axis, note in transformed["axes"].items():
        lines.append(f"- **{axis}**: {note}")
    lines += ["", "## Cambios aplicados", ""]
    lines += [f"- {c}" for c in transformed["changes"]] or ["- (ningun termino absoluto sustituido)"]
    lines += ["", "## Evidencia que falta", ""]
    lines += [f"- {e}" for e in transformed["evidence_needed"]] or ["- (ninguna: el texto ya trae cifras y fuente)"]
    lines += ["",
              "## Dictamen CENTRO Guard (simulado)", "",
              f"- **Veredicto: {verdict['decision']}** (regla que decide: {verdict['deciding_rule']})",
              f"- {verdict['reason']}",
              f"- Reversibilidad efectiva: {verdict['reversibility_class_effective']} | Evidencia: {verdict['evidence_state']}",
              "- " + verdict["binding_warning"], "",
              "## Registro LUCEM", "",
              f"- Entrada `{log['id']}` · hash `{log['hash'][:16]}...` · total {log['entries_total']}", "",
              "_Propuesta, no validacion. CENTRO-001 es un protocolo propuesto sin ejecutar._"]
    return "\n".join(lines) + "\n"


def cmd_renovar(args):
    text = _read_input(args)
    transformed = tool_transform(text, focus=args.focus)
    verdict = tool_centro_evaluate(
        action=args.operation or "Publicar el texto renovado",
        operation=args.operation or "publicar_texto",
        resource=args.resource or "texto_renovado",
        authority_verified=args.authority_verified,
        authority_identity=args.authority_identity,
        evidence_state=args.evidence_state,
        reversibility_class=args.reversibility_class,
        human_approval=args.human_approval,
        human_approval_specific=args.human_approval,
        displaces_harm=args.displaces_harm,
        critical_uncertainty=args.critical_uncertainty)
    log = tool_lucem_log(f"Renovacion A->A' registrada: veredicto {verdict['decision']} sobre '{text[:80]}'",
                         source="renova.py renovar", confidence="propuesta",
                         tags=["renova", "A->A'", verdict["decision"]])
    out = _md_renovacion(text, transformed, verdict, log)
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"Escrito en {args.out}")
    print(out)
    return 0


def _print_json(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(prog="renovar", description="Bot Renova: A -> A' + CENTRO Guard (simulado) + LUCEM")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("search", help="Buscar en el corpus")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--source", default="all", choices=["all", "staging", "biblioteca", "fundamento"])

    p = sub.add_parser("document", help="Leer un documento integro")
    p.add_argument("name")

    p = sub.add_parser("scenario", help="Escenario R-001..R-040")
    p.add_argument("case_id")

    sub.add_parser("state", help="Estado del servidor y del corpus")

    p = sub.add_parser("evaluate", help="Evaluar una accion con CENTRO Guard (simulado)")
    p.add_argument("action")
    p.add_argument("--operation")
    p.add_argument("--resource")
    p.add_argument("--authority-verified", action="store_true")
    p.add_argument("--authority-identity")
    p.add_argument("--evidence-state", default="Faltante", choices=["Confirmada", "Faltante", "Inferida", "No_verificable"])
    p.add_argument("--reversibility-class", default="unknown", choices=["R0", "R1", "R2", "R3", "unknown"])
    p.add_argument("--human-approval", action="store_true")
    p.add_argument("--human-approval-specific", action="store_true",
                   help="Aprobacion humana especifica para esta operacion y recurso (RNV-05 en R2/R3)")
    p.add_argument("--displaces-harm", action="store_true")
    p.add_argument("--affected-approval", action="store_true",
                   help="Autorizacion de los afectados (RNV-03 con displaces_harm)")
    p.add_argument("--critical-uncertainty", action="store_true")

    p = sub.add_parser("transform", help="Renovar un texto (A -> A')")
    p.add_argument("text", nargs="+")
    p.add_argument("--focus")

    p = sub.add_parser("compare", help="Comparar tratamiento vs baseline (EGRA, simulado)")
    p.add_argument("treatment")
    p.add_argument("baseline")
    p.add_argument("--criteria", help="JSON: [{\"name\":..., \"weight\":1, \"treatment_score\":7, \"baseline_score\":5}]")

    p = sub.add_parser("log", help="Registrar evidencia en LUCEM")
    p.add_argument("entry")
    p.add_argument("--source")
    p.add_argument("--confidence")

    # Pipeline por defecto: renovar. El texto llega como argumento suelto
    # (sin subcomando), por --text, por --file o por stdin.
    parser.add_argument("--text", nargs="+", help="Texto a renovar")
    parser.add_argument("--file")
    parser.add_argument("--out")
    parser.add_argument("--focus")
    parser.add_argument("--operation")
    parser.add_argument("--resource")
    parser.add_argument("--authority-verified", action="store_true")
    parser.add_argument("--authority-identity")
    parser.add_argument("--evidence-state", default="Faltante", choices=["Confirmada", "Faltante", "Inferida", "No_verificable"])
    parser.add_argument("--reversibility-class", default="unknown", choices=["R0", "R1", "R2", "R3", "unknown"])
    parser.add_argument("--human-approval", action="store_true")
    parser.add_argument("--displaces-harm", action="store_true")
    parser.add_argument("--critical-uncertainty", action="store_true")
    raw = sys.argv[1:]
    subcommands = {"search", "document", "scenario", "state", "evaluate", "transform", "compare", "log"}
    if raw and not raw[0].startswith("-") and raw[0] not in subcommands:
        args = parser.parse_args(["--text"] + raw)
    else:
        args = parser.parse_args()

    if args.command == "search":
        _print_json(tool_search(args.query, args.limit, args.source))
    elif args.command == "document":
        _print_json(tool_get_document(args.name))
    elif args.command == "scenario":
        _print_json(tool_benchmark_scenario(args.case_id))
    elif args.command == "state":
        _print_json(tool_get_state())
    elif args.command == "evaluate":
        # --human-approval implica especifica si no se pasa el flag
        # separado (compatibilidad con el comportamiento anterior).
        specific = args.human_approval_specific or args.human_approval
        _print_json(tool_centro_evaluate(args.action, args.operation, args.resource,
                                         args.authority_verified, args.authority_identity,
                                         args.evidence_state, args.reversibility_class,
                                         args.human_approval, specific,
                                         args.displaces_harm, args.affected_approval, args.critical_uncertainty))
    elif args.command == "transform":
        _print_json(tool_transform(" ".join(args.text), args.focus))
    elif args.command == "compare":
        try:
            criteria = json.loads(args.criteria) if args.criteria else None
        except json.JSONDecodeError as exc:
            raise SystemExit(f"error: --criteria no es JSON valido: {exc}")
        _print_json(tool_egra_compare(args.treatment, args.baseline, criteria))
    elif args.command == "log":
        _print_json(tool_lucem_log(args.entry, args.source, args.confidence))
    else:
        return cmd_renovar(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
