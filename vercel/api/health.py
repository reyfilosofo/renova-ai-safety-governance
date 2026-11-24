"""GET /health for the Renova MCP server on Vercel (same payload as local)."""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("RENOVA_STAGING_DIR", str(ROOT / "corpus" / "staging"))
os.environ.setdefault("RENOVA_BIBLIOTECA_DIR", str(ROOT / "corpus" / "biblioteca"))
os.environ.setdefault("RENOVA_INVENTARIO_JSON", str(ROOT / "corpus" / "inventario.json"))
os.environ.setdefault("RENOVA_DATA_DIR", "/tmp/renova-data")

import renova_server as renova_server  # noqa: E402


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = {"status": "ok", "server": "renova-mcp",
                   "version": renova_server.SERVER_VERSION,
                   "tools": [t["name"] for t in renova_server.TOOLS]}
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass
