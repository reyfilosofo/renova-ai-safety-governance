#!/bin/sh
# Arranque del servidor MCP Renova (canónico, solo stdlib, sin dependencias).
# Uso: ./start.sh [--http --port 8765 | --stdio]
# Solo localhost: el modo --http escucha en 127.0.0.1, nunca en 0.0.0.0.
#
# El corpus es la raíz de este repositorio:
#   - docs/, benchmark/, centro-guard-policy.yaml, README.md, packages/
#   - renova-fundamento-inventario-drive.json (metadatos, en la raíz)
# La Biblioteca (texto extraído de 24 obras) NO está en el repo por
# tamaño y derechos: sin ella el servidor degrada con gracia.
set -e
cd "$(dirname "$0")"
export RENOVA_STAGING_DIR="$PWD/.."
export RENOVA_INVENTARIO_JSON="$PWD/../renova-fundamento-inventario-drive.json"
# RENOVA_BIBLIOTECA_DIR: opcional. Sin ella el servidor degrada con gracia.
if [ -d "$PWD/../biblioteca" ]; then
  export RENOVA_BIBLIOTECA_DIR="$PWD/../biblioteca"
fi
export RENOVA_DATA_DIR="$PWD/data"
mkdir -p "$RENOVA_DATA_DIR"
exec python3 server.py "$@"
