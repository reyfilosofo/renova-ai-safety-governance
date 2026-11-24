"""WSGI entrypoint for the Renova MCP server on Vercel (stdlib only).

Vercel's Python runtime loads a supported entrypoint file that defines
``app`` (see vercel.com/docs/functions/runtimes/python). A root
``server.py`` was auto-detected as that entrypoint before, but it defined
no ``app`` — the runtime ran its BaseHTTPRequestHandler instead and the
vercel.json rewrites mangled the paths it saw (/health -> /api/health),
so /health and /mcp 404'd. The canonical server now lives as
``renova_server.py`` (not an entrypoint name) and THIS file is the only
entrypoint: a plain WSGI app that routes every request itself.

Routes (tolerant of the /api/* aliases, in case a rewrite still applies):
  GET  /health, /api/health -> {"status": "ok", ...} with the 8 tools
  GET  /, /mcp, /api/mcp    -> server info JSON
  POST /mcp, /api/mcp       -> MCP Streamable HTTP (handle_request)
  anything else             -> 404 {"error": "not found"}

Stateless: handle_request keeps no session server-side. LUCEM writes to
/tmp on Vercel (ephemeral); the durable log lives on the local server.
No auth yet: the public endpoint has no OAuth. CENTRO verdicts remain
simulated; the server executes no real action.

Sin autenticacion global por decision explicita (las conexiones
verificadas de ChatGPT/Grok/Gemini-CLI son sin auth y anadir auth las
romperia). Mitigacion minima: limite de cuerpo 1 MB (413 antes de leer),
rate limit 60 peticiones/minuto por IP (429) y renova_lucem_log
DESACTIVADO en este endpoint publico (RENOVA_PUBLIC_ENDPOINT=1: la
unica escritura publica queda bloqueada para que nadie envenene el
registro de evidencia; ver renova_core.tool_lucem_log).
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("RENOVA_STAGING_DIR", str(ROOT / "corpus" / "staging"))
os.environ.setdefault("RENOVA_BIBLIOTECA_DIR", str(ROOT / "corpus" / "biblioteca"))
os.environ.setdefault("RENOVA_INVENTARIO_JSON", str(ROOT / "corpus" / "inventario.json"))
os.environ.setdefault("RENOVA_DATA_DIR", "/tmp/renova-data")
# H-01: endpoint publico -> escritura LUCEM desactivada (antes de importar).
os.environ["RENOVA_PUBLIC_ENDPOINT"] = "1"

import renova_server  # noqa: E402


def _body(payload):
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")


def _respond(start_response, status, payload, session_id=None):
    body = _body(payload)
    headers = [("Content-Type", "application/json"),
               ("Content-Length", str(len(body)))]
    if session_id:
        headers.append(("Mcp-Session-Id", session_id))
    start_response(status, headers)
    return [body]


def app(environ, start_response):
    import uuid

    method = environ.get("REQUEST_METHOD", "GET")
    path = (environ.get("PATH_INFO") or "/").rstrip("/") or "/"

    if method == "GET" and path in ("/health", "/api/health"):
        return _respond(start_response, "200 OK",
                        {"status": "ok", "server": "renova-mcp",
                         "version": renova_server.SERVER_VERSION,
                         "handler": "app.py (WSGI)",
                         "tools": [t["name"] for t in renova_server.TOOLS]})
    if method == "GET" and path in ("/", "/mcp", "/api/mcp"):
        return _respond(start_response, "200 OK",
                        {"server": "renova-mcp",
                         "version": renova_server.SERVER_VERSION,
                         "protocol": "MCP Streamable HTTP",
                         "endpoint": "POST /mcp",
                         "note": "Prototipo de laboratorio. Veredictos CENTRO simulados."})
    if method == "POST" and path in ("/mcp", "/api/mcp"):
        # A14: Content-Type presente y distinto de application/json
        # (se admite charset) -> 415. Si falta, se acepta: los clientes
        # ya verificados no siempre lo envian.
        content_type = environ.get("CONTENT_TYPE")
        if content_type is not None and content_type.split(";")[0].strip().lower() != "application/json":
            return _respond(start_response, "415 Unsupported Media Type",
                            {"error": "content-type must be application/json"})
        # A10(c): Accept solo con advertencia en stderr; rechazar
        # romperia a los clientes ya verificados.
        accept = environ.get("HTTP_ACCEPT") or ""
        if "application/json" not in accept and "text/event-stream" not in accept:
            print(f"ADVERTENCIA renova-mcp: POST /mcp sin Accept application/json "
                  f"(recibido: {accept!r}); se acepta por compatibilidad con clientes verificados",
                  file=sys.stderr)
        try:
            length = int(environ.get("CONTENT_LENGTH") or 0)
        except ValueError:
            length = 0
        # A1/H-01: cuerpo > 1 MB -> 413 ANTES de leerlo.
        if length > renova_server.MAX_BODY_BYTES:
            return _respond(start_response, "413 Payload Too Large",
                            {"error": "payload too large"})
        # A1/H-01: rate limit 60 peticiones/minuto por IP -> 429.
        # (En Vercel no hace falta semaforo de hilos: la plataforma
        # gestiona la concurrencia.)
        forwarded = environ.get("HTTP_X_FORWARDED_FOR") or ""
        client_ip = forwarded.split(",")[0].strip() or environ.get("REMOTE_ADDR") or "unknown"
        if not renova_server._check_rate_limit(client_ip):
            return _respond(start_response, "429 Too Many Requests",
                            {"error": "rate limit"})
        raw = environ["wsgi.input"].read(length) if length > 0 else b""
        session_id = environ.get("HTTP_MCP_SESSION_ID") or uuid.uuid4().hex
        try:
            msg = json.loads(raw.decode("utf-8"))
        except Exception:
            return _respond(start_response, "400 Bad Request",
                            {"jsonrpc": "2.0", "id": None,
                             "error": {"code": -32700, "message": "Parse error"}},
                            session_id)
        try:
            resp = renova_server.handle_request(msg)
        except renova_server.McpError as exc:
            resp = {"jsonrpc": "2.0", "id": msg.get("id") if isinstance(msg, dict) else None,
                    "error": {"code": exc.code, "message": exc.message}}
        except Exception as exc:  # noqa: BLE001
            resp = {"jsonrpc": "2.0", "id": msg.get("id") if isinstance(msg, dict) else None,
                    "error": {"code": -32603, "message": f"Internal error: {exc}"}}
        if resp is None:
            # H-06: 202 con cuerpo {} igual que server.py (antes vacio).
            return _respond(start_response, "202 Accepted", {}, session_id)
        return _respond(start_response, "200 OK", resp, session_id)
    return _respond(start_response, "404 Not Found", {"error": "not found"})
