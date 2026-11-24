# Servidor MCP Renova — solo stdlib, sin dependencias de Python.
# Construir:  docker build -t renova-mcp .
# Correr (local): docker run --rm -p 8765:8765 renova-mcp
# NO desplegado en publico: hosting y licencia pendientes de decision de Rey.
FROM python:3.12-slim
WORKDIR /app
COPY server.py renova_core.py ./
# El corpus se monta en tiempo de ejecucion (no se copia en la imagen):
#   -v <repo>:/corpus/staging:ro
#     (la raíz del repo: docs/, benchmark/, centro-guard-policy.yaml)
#   -v <repo>/renova-fundamento-inventario-drive.json:/corpus/inventario.json:ro
#   -v renova-data:/app/data
ENV RENOVA_STAGING_DIR=/corpus/staging
ENV RENOVA_BIBLIOTECA_DIR=/corpus/biblioteca
ENV RENOVA_INVENTARIO_JSON=/corpus/inventario.json
ENV RENOVA_DATA_DIR=/app/data
ENV PYTHONUNBUFFERED=1
EXPOSE 8765
CMD ["python3", "server.py", "--http", "--host", "0.0.0.0", "--port", "8765"]
