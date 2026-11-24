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
                         "tools": [t["name"] for t in renova_server.TOOLS]})
    if method == "GET" and path in ("/", "/mcp", "/api/mcp"):
        return _respond(start_response, "200 OK",
                        {"server": "renova-mcp",
                         "version": renova_server.SERVER_VERSION,
                         "protocol": "MCP Streamable HTTP",
                         "endpoint": "POST /mcp",
                         "note": "Prototipo de laboratorio. Veredictos CENTRO simulados."})
    if method == "POST" and path in ("/mcp", "/api/mcp"):
        try:
            length = int(environ.get("CONTENT_LENGTH") or 0)
        except ValueError:
            length = 0
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
            resp = {"jsonrpc": "2.0", "id": msg.get("id"),
                    "error": {"code": exc.code, "message": exc.message}}
        except Exception as exc:  # noqa: BLE001
            resp = {"jsonrpc": "2.0", "id": msg.get("id"),
                    "error": {"code": -32603, "message": f"Internal error: {exc}"}}
        if resp is None:
            start_response("202 Accepted",
                           [("Mcp-Session-Id", session_id),
                            ("Content-Length", "0")])
            return [b""]
        return _respond(start_response, "200 OK", resp, session_id)
    return _respond(start_response, "404 Not Found", {"error": "not found"})
