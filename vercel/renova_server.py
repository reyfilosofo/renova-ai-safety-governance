#!/usr/bin/env python3
"""Servidor MCP Renova (stdlib, sin dependencias).

Modos:
  python3 server.py --stdio          (por defecto; para clientes MCP locales)
  python3 server.py --http [--port 8765] [--host 127.0.0.1]

Protocolo MCP Streamable HTTP 2025-11-25 / 2025-06-18 / 2025-03-26.
Las herramientas son las de renova_core.py. Ninguna ejecuta acciones
reales con privilegios: renova_centro_evaluate es un veredicto simulado.
"""
from __future__ import annotations

import argparse
import json
import sys
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from renova_core import (CORPUS, SERVER_VERSION, tool_benchmark_scenario,
                         tool_centro_evaluate, tool_egra_compare,
                         tool_get_document, tool_get_state, tool_lucem_log,
                         tool_search, tool_transform)

PROTOCOLS = ("2025-11-25", "2025-06-18", "2025-03-26")
SERVER_INFO = {"name": "renova-mcp", "version": SERVER_VERSION}

TOOLS = [
    {"name": "renova_search", "description": "Busca texto completo en los docs del staging, en las 16 obras de la Biblioteca (texto extraido) y en los metadatos de las 54 obras de Fundamento. No inventa texto de libros no leidos.",
     "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}, "limit": {"type": "integer", "default": 10}, "source": {"type": "string", "enum": ["all", "staging", "biblioteca", "fundamento"], "default": "all"}}, "required": ["query"]}},
    {"name": "renova_get_document", "description": "Devuelve integro un documento del staging (los 3 fundacionales, verbatim).",
     "inputSchema": {"type": "object", "properties": {"name": {"type": "string", "description": "Nombre del documento, p. ej. resumen-publico, limites-declarados, centro-001-protocolo"}}, "required": ["name"]}},
    {"name": "renova_centro_evaluate", "description": "Evalua una accion propuesta con RNV-01 a RNV-06 (CENTRO Guard v1.0). Veredicto SIMULADO: DENY / REVIEW / ALLOW_SIMULATED. Nunca ejecuta ni bloquea una accion real.",
     "inputSchema": {"type": "object", "properties": {
         "action": {"type": "string"}, "operation": {"type": "string"}, "resource": {"type": "string"},
         "authority_verified": {"type": "boolean", "default": False}, "authority_identity": {"type": "string"},
         "evidence_state": {"type": "string", "enum": ["Confirmada", "Faltante", "Inferida", "No_verificable"], "default": "Faltante"},
         "reversibility_class": {"type": "string", "enum": ["R0", "R1", "R2", "R3", "unknown"], "default": "unknown"},
         "human_approval": {"type": "boolean", "default": False}, "human_approval_specific": {"type": "boolean", "default": False},
         "displaces_harm": {"type": "boolean", "default": False}, "affected_approval": {"type": "boolean", "default": False},
         "critical_uncertainty": {"type": "boolean", "default": False}}, "required": ["action"]}},
    {"name": "renova_benchmark_scenario", "description": "Devuelve un escenario R-001 a R-040 del Benchmark R v0.1 con su etiqueta de autor; gold_label siempre null (revision ciega pendiente).",
     "inputSchema": {"type": "object", "properties": {"case_id": {"type": "string"}}, "required": ["case_id"]}},
    {"name": "renova_transform", "description": "Proceso A -> A' (Renova): renueva un texto con los ejes CLARITAS / RATIO / VITA / CENTRO. Propuesta de redaccion, no validacion.",
     "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}, "focus": {"type": "string"}}, "required": ["text"]}},
    {"name": "renova_egra_compare", "description": "Compara tratamiento vs baseline con criterios y puntuaciones explicitas aportadas por quien llama. Si faltan puntuaciones, no se inventan. Resultado simulado.",
     "inputSchema": {"type": "object", "properties": {
         "treatment": {"type": "string"}, "baseline": {"type": "string"}, "metric_name": {"type": "string"}, "sample_size": {"type": "integer"},
         "criteria": {"type": "array", "items": {"type": "object", "properties": {"name": {"type": "string"}, "weight": {"type": "number"}, "treatment_score": {"type": "number"}, "baseline_score": {"type": "number"}}, "required": ["name"]}}}, "required": ["treatment", "baseline"]}},
    {"name": "renova_lucem_log", "description": "Anade una entrada al registro local de evidencia LUCEM (JSONL con hash encadenado) y devuelve su id y hash.",
     "inputSchema": {"type": "object", "properties": {"entry": {"type": "string"}, "source": {"type": "string"}, "confidence": {"type": "string"}, "tags": {"type": "array", "items": {"type": "string"}}}, "required": ["entry"]}},
    {"name": "renova_get_state", "description": "Estado real del servidor, conteos del corpus indexado, version de la politica CENTRO Guard y limites declarados.",
     "inputSchema": {"type": "object", "properties": {}}},
]

DISPATCH = {
    "renova_search": lambda a: tool_search(a.get("query", ""), a.get("limit", 10), a.get("source", "all")),
    "renova_get_document": lambda a: tool_get_document(a.get("name", "")),
    "renova_centro_evaluate": lambda a: tool_centro_evaluate(**{k: v for k, v in a.items()}),
    "renova_benchmark_scenario": lambda a: tool_benchmark_scenario(a.get("case_id", "")),
    "renova_transform": lambda a: tool_transform(a.get("text", ""), a.get("focus")),
    "renova_egra_compare": lambda a: tool_egra_compare(a.get("treatment", ""), a.get("baseline", ""), a.get("criteria"), a.get("metric_name"), a.get("sample_size")),
    "renova_lucem_log": lambda a: tool_lucem_log(a.get("entry", ""), a.get("source"), a.get("confidence"), a.get("tags")),
    "renova_get_state": lambda a: tool_get_state(),
}


class McpError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message


def handle_request(msg):
    """Procesa un mensaje JSON-RPC MCP y devuelve la respuesta (o None)."""
    if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0":
        raise McpError(-32600, "Invalid Request")
    method = msg.get("method", "")
    req_id = msg.get("id")
    is_notification = req_id is None
    params = msg.get("params") or {}

    def result(payload):
        return None if is_notification else {"jsonrpc": "2.0", "id": req_id, "result": payload}

    if method == "initialize":
        version = params.get("protocolVersion")
        negotiated = version if version in PROTOCOLS else "2025-06-18"
        return result({"protocolVersion": negotiated,
                       "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
                       "serverInfo": SERVER_INFO})
    if method in ("notifications/initialized", "notifications/cancelled"):
        return None
    if method == "ping":
        return result({})
    if method == "tools/list":
        return result({"tools": TOOLS})
    if method == "tools/call":
        name = params.get("name", "")
        args = params.get("arguments") or {}
        if name not in DISPATCH:
            raise McpError(-32602, f"Unknown tool: {name}")
        try:
            output = DISPATCH[name](args)
        except (ValueError, TypeError) as exc:
            return result({"content": [{"type": "text", "text": f"error: {exc}"}], "isError": True})
        if isinstance(output, dict) and output.get("error"):
            return result({"content": [{"type": "text", "text": json.dumps(output, ensure_ascii=False)}], "isError": True})
        text = json.dumps(output, ensure_ascii=False, indent=2)
        return result({"content": [{"type": "text", "text": text}], "structuredContent": output})
    if method == "resources/list":
        resources = [{"uri": f"renova://docs/{name}", "name": name, "title": doc["title"], "mimeType": "text/markdown"}
                     for name, doc in CORPUS.staging_docs.items()]
        return result({"resources": resources})
    if method == "resources/read":
        uri = params.get("uri", "")
        name = uri.rsplit("/", 1)[-1]
        if name not in CORPUS.staging_docs:
            raise McpError(-32602, f"Unknown resource: {uri}")
        doc = CORPUS.staging_docs[name]
        return result({"contents": [{"uri": uri, "mimeType": "text/markdown", "text": doc["text"]}]})
    if method == "prompts/list":
        return result({"prompts": [{"name": "renovar", "description": "Renueva un texto con A -> A' y lo somete a CENTRO Guard (simulado).",
                                    "arguments": [{"name": "text", "description": "Texto o idea a renovar", "required": True}]}]})
    if method == "prompts/get":
        if params.get("name") != "renovar":
            raise McpError(-32602, f"Unknown prompt: {params.get('name')}")
        text = params.get("arguments", {}).get("text", "")
        return result({"messages": [{"role": "user", "content": {"type": "text", "text": f"Renueva este texto con Renova (A -> A') y evalualo con CENTRO Guard: {text}"}}]})
    raise McpError(-32601, f"Method not found: {method}")


def serve_stdio():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}) + "\n")
            sys.stdout.flush()
            continue
        try:
            resp = handle_request(msg)
        except McpError as exc:
            resp = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": exc.code, "message": exc.message}}
        except Exception as exc:  # noqa: BLE001 - el servidor no debe morir por una llamada
            resp = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": -32603, "message": f"Internal error: {exc}"}}
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):  # silencio en logs
        pass

    def _send_json(self, status, payload, session_id=None):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        if session_id:
            self.send_header("Mcp-Session-Id", session_id)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send_json(200, {"status": "ok", "server": "renova-mcp", "version": SERVER_VERSION,
                                  "tools": [t["name"] for t in TOOLS]})
        elif self.path in ("/", "/mcp"):
            self._send_json(200, {"server": "renova-mcp", "version": SERVER_VERSION,
                                  "protocol": "MCP Streamable HTTP", "endpoint": "POST /mcp",
                                  "note": "Prototipo de laboratorio. Sin autenticacion en local; la via remota con OAuth queda para el despliegue publico."})
        else:
            self._send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/mcp":
            self._send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length)
        session_id = self.headers.get("Mcp-Session-Id") or uuid.uuid4().hex
        try:
            msg = json.loads(raw.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            self._send_json(400, {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}, session_id)
            return
        try:
            resp = handle_request(msg)
        except McpError as exc:
            resp = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": exc.code, "message": exc.message}}
        except Exception as exc:  # noqa: BLE001
            resp = {"jsonrpc": "2.0", "id": msg.get("id"), "error": {"code": -32603, "message": f"Internal error: {exc}"}}
        if resp is None:
            self._send_json(202, {}, session_id)
        else:
            self._send_json(200, resp, session_id)


def main():
    parser = argparse.ArgumentParser(description="Servidor MCP Renova")
    parser.add_argument("--stdio", action="store_true", help="Modo stdio (por defecto)")
    parser.add_argument("--http", action="store_true", help="Modo HTTP local")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if args.http:
        server = ThreadingHTTPServer((args.host, args.port), Handler)
        print(f"renova-mcp {SERVER_VERSION} escuchando en http://{args.host}:{args.port}/mcp", flush=True)
        print("Prototipo de laboratorio. Solo local: no exponer sin autenticacion.", flush=True)
        server.serve_forever()
    else:
        serve_stdio()


if __name__ == "__main__":
    main()
