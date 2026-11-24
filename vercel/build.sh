#!/bin/bash
# Ensambla el paquete de despliegue Vercel desde las fuentes canónicas.
# No toca nada fuera de ~/workspace/renova-mcp-server ni de los corpus
# canónicos. Regenera corpus/ (salida de build, excluida de git).
set -euo pipefail
WS="$HOME/workspace"
DEST="$(cd "$(dirname "$0")" && pwd)"
cp "$WS/renova-mcp-server/server.py" "$WS/renova-mcp-server/renova_core.py" "$DEST/"
cp "$WS/renova-mcp-server/requirements.txt" "$DEST/" 2>/dev/null || echo "" > "$DEST/requirements.txt"
rm -rf "$DEST/corpus"
mkdir -p "$DEST/corpus/staging" "$DEST/corpus/biblioteca/txt"
cp -r "$WS/renova-ai-safety-governance-staging/"* "$DEST/corpus/staging/"
cp "$WS/renova-fundamento-inventario-drive.json" "$DEST/corpus/inventario.json"
cp "$WS/renova-biblioteca-2026-11-10/txt/"*.txt "$DEST/corpus/biblioteca/txt/"
python3 -m py_compile "$DEST/server.py" "$DEST/renova_core.py" "$DEST/api/mcp.py" "$DEST/api/health.py"
echo "Paquete Vercel listo en $DEST"
du -sh "$DEST"
find "$DEST" -type f | wc -l
