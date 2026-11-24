"""Vercel serverless wrapper for the canonical Renova MCP server (stdlib).

Vercel Python runtime: files in api/ are serverless functions; a class
named `handler` extending BaseHTTPRequestHandler is the entrypoint.
This wrapper reuses the canonical server.py handle_request() and
renova_core.py from the project root (copied there by build.sh), with the
corpus under corpus/. No new tools, no new behaviour: the same 8 tools.

Stateless: the canonical server does not keep sessions server-side
(handle_request ignores the session id), so serverless invocations work.
LUCEM writes to /tmp on Vercel: ephemeral per invocation — the durable
LUCEM log lives on the local server (renova-mcp-server/data/lucem.jsonl).

No auth yet: the public endpoint has no OAuth. Do not expose privileged
actions through it; CENTRO verdicts remain simulated.
"""
import json
import os
import sys
import uuid
from http.server import BaseHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("RENOVA_STAGING_DIR", str(ROOT / "corpus" / "staging"))
os.environ.setdefault("RENOVA_BIBLIOTECA_DIR", str(ROOT / "corpus" / "biblioteca"))
os.environ.setdefault("RENOVA_INVENTARIO_JSON", str(ROOT / "corpus" / "inventario.json"))
os.environ.setdefault("RENOVA_DATA_DIR", "/tmp/renova-data")

import server as renova_server  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Mcp-Session-Id", uuid.uuid4().hex)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, {"server": "renova-mcp", "version": renova_server.SERVER_VERSION,
                         "protocol": "MCP Streamable HTTP", "endpoint": "POST /mcp",
                         "note": "Prototipo de laboratorio. Veredictos CENTRO simulados."})

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length)
        try:
            msg = json.loads(raw.decode("utf-8"))
        except Exception:
            self._send(400, {"jsonrpc": "2.0", "id": None,
                             "error": {"code": -32700, "message": "Parse error"}})
            return
        try:
            resp = renova_server.handle_request(msg)
        except renova_server.McpError as exc:
            resp = {"jsonrpc": "2.0", "id": msg.get("id"),
                    "error": {"code": exc.code, "message": exc.message}}
        except Exception as exc:  # noqa: BLE001
            resp = {"jsonrpc": "2.0", "id": msg.get("id"),
                    "error": {"code": -32603, "message": f"Internal error: {exc}"}}
        if resp is None:
            self.send_response(202)
            self.send_header("Mcp-Session-Id", uuid.uuid4().hex)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        self._send(200, resp)

    def log_message(self, *args):
        pass
