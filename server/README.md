# Servidor MCP ℛenova — funcional, local, solo stdlib

Servidor MCP (Model Context Protocol) del programa **RENOVA AI SAFETY &
GOVERNANCE**, de Rey Filósofo / SERESARTE / ℛenova. Sin dependencias: solo
Python 3.10+ de la biblioteca estándar. No hay SDK de MCP instalado en
esta máquina, así que el protocolo (JSON-RPC, Streamable HTTP y stdio) está
implementado a mano en `server.py`.

> **Estado honesto, siempre visible:** prototipo de laboratorio.
> CENTRO-001 es un protocolo propuesto, no ejecutado y sin resultados.
> CENTRO Guard no está validado: sus veredictos son simulados
> (`DENY` / `REVIEW` / `ALLOW_SIMULATED`) y nunca ejecutan ni bloquean
> una acción real. Los resultados sintéticos no son validación externa.
> Sin respaldo de NIST, ISO ni OWASP. **UNLICENSED** (sin licencia:
> no compartir en público hasta decidirla).

## Qué hace (8 herramientas, todas funcionales)

| Herramienta | Qué hace de verdad |
|---|---|
| `renova_search` | Búsqueda de texto completo sobre los docs del staging, las 16 obras de la Biblioteca (texto extraído, 1,6 M de palabras) y los metadatos de las 54 obras de Fundamento |
| `renova_get_document` | Devuelve íntegro el documento pedido (los 3 fundacionales, verbatim) |
| `renova_centro_evaluate` | Implementa RNV-01 a RNV-06 leyendo `centro-guard-policy.yaml`: devuelve DENY / REVIEW / ALLOW_SIMULATED con la regla que decide y el chequeo por política |
| `renova_benchmark_scenario` | Devuelve el escenario R-001..R-040 parseado del diseño; `gold_label` siempre null (revisión ciega pendiente) |
| `renova_transform` | Proceso A → A′ con CLARITAS / RATIO / VITA / CENTRO, con cambios listados y evidencia que falta. Propuesta, no validación |
| `renova_egra_compare` | Compara tratamiento vs baseline con criterios y puntuaciones explícitas; si faltan puntuaciones, no las inventa |
| `renova_lucem_log` | Añade una entrada al registro local de evidencia (`data/lucem.jsonl`, hash encadenado SHA-256) y devuelve su id |
| `renova_get_state` | Estado real, conteos del corpus indexado, versión de la política y límites |

## Arrancar el servidor

```bash
# stdio (para clientes MCP locales: Claude Desktop, etc.)
python3 server.py --stdio

# HTTP local (para Muse, vía el conector custom.renova)
python3 server.py --http --port 8765
# Salud:  curl http://127.0.0.1:8765/health
```

O con `start.sh`, que apunta el corpus a la raíz de este repo:

```bash
./start.sh --http --port 8765
```

Nota: al clonar por git o descargar por web, los scripts pueden perder
el bit ejecutable. Si `./renovar` o `./start.sh` dan «Permission
denied», ejecuta `chmod +x renovar start.sh` o invócalos con
`sh start.sh` / `python3 renova.py`.

## El bot `renovar`

```bash
./renovar "La IA siempre tiene la razón y todos deben obedecerla"
./renovar --file texto.md --out renovado.md
./renovar search "CENTRO Guard"
./renovar document limites-declarados
./renovar scenario R-021
./renovar state
./renovar evaluate "Publicar el informe" --reversibility-class R3 --evidence-state Faltante
```

`renovar` corre el pipeline completo: `renova_transform` +
`renova_centro_evaluate` + `renova_lucem_log`, y emite markdown con la
renovación, su dictamen simulado y su registro LUCEM.

## Conector para Muse

Ver `~/workspace/custom-connectors/custom.renova/CONNECTOR.md`:

```bash
python3 ~/workspace/custom-connectors/custom.renova/bin/local_client.py list-tools
echo '{"query": "CENTRO Guard"}' > /tmp/args.json
python3 ~/workspace/custom-connectors/custom.renova/bin/local_client.py call-tool --name renova_search --arguments-file /tmp/args.json
```

El servidor local no necesita credencial. La vía remota con OAuth queda
para el despliegue público.

## Config para Claude / ChatGPT (no desplegado)

En `configs/`:

- `claude_desktop_config.json` — servidor stdio local para Claude Desktop.
  Apunta a `<clon-del-repo>/server/server.py --stdio`: ajusta la ruta a
  donde clones este repo. En Claude Desktop: Settings → Developer →
  Edit Config, pegar el contenido y reiniciar. Es local, no necesita
  endpoint público.
- `chatgpt_mcp_config.json` — plantilla para un servidor MCP remoto. Su
  URL es un ejemplo que **no existe**: no hay endpoint HTTPS público
  todavía. Cuando el despliegue público tenga URL real, sustituirla aquí.

Ambas configs están marcadas como no desplegadas hasta que Rey decida
el hosting público y la licencia.

## Activación (2026-11-23)

Estado completo por plataforma en `ACTIVATION.md`. Resumen: servidor
local activo en `127.0.0.1:8765` (PID en `server.pid`); despliegue
público intentado y bloqueado (Vercel 403 equipo seresarte, Replit
Unauthorized) con el paquete listo en `vercel-deploy/` (no incluido en
este repo); Drive verificado (carpeta privada `RENOVA-MCP`); repo GitHub
creado 2026-11-23 20:23 CST con los documentos (commit `79866df7`) y el
código del servidor en `server/` de este repo (paquete limpio, sin
`.git/`); Grok/Gemini solo por puente (`docs/bridges/`). Licencia
UNLICENSED, pendiente. Sin arranque automático tras reinicio de la VM:
ver `ACTIVATION.md`, fila «Persistencia local».

Versiones fijadas: Python 3.12.3, solo biblioteca estándar, cero
dependencias externas. Sin SDK de MCP instalado: el protocolo (JSON-RPC,
Streamable HTTP y stdio) está implementado a mano en `server.py`.

## Despliegue remoto (no desplegado)

`Dockerfile` incluido (imagen `python:3.12-slim`, solo stdlib, puerto
8765). Pasos cuando Rey lo autorice:

1. Decidir la licencia (hoy UNLICENSED) y crear el repo público
   `renova-ai-safety-governance` a mano en github.com/new (el intento
   automático devolvió 403). Hecho: repo creado 2026-11-23 20:23 CST,
   código en `server/` de este repo.
2. Desplegar en Vercel o Cloudflare (ver `Dockerfile` y las notas al
   final) con HTTPS y OAuth (registro dinámico, `resource` canónico).
3. Sustituir el endpoint de ejemplo en
   `~/workspace/custom-connectors/custom.renova/bin/mcp_client.py` y
   registrar la conexión con `credentials.request_api_access`.
4. Probar con una lectura inofensiva (`renova_get_state`) antes de
   anunciar el endpoint.

## Corpus (de dónde sale cada dato)

Detalle completo (método, supuestos, límites, falsabilidad) en
`CORPUS.md`. Resumen:

- La raíz de este repo — `docs/` (11 docs), `benchmark/` (diseño v0.1,
  lote R-001–R-040), `centro-guard-policy.yaml`, `README.md`,
  `packages/PACKAGES.md` — es el staging que indexa el servidor
  (`RENOVA_STAGING_DIR`, ver `start.sh`). Texto completo indexado.
- `renova-fundamento-inventario-drive.json` (raíz del repo) —
  metadatos verificados de las 54 obras de Fundamento. **Solo
  metadatos**: sus PDF completos no están en el repo y el servidor lo
  dice así; no inventa texto de libros que no leyó.
- La Biblioteca (texto extraído de 24 obras, 4.478 págs., 1.869.502
  palabras) **no está en el repo** por tamaño y derechos. Sin ella el
  servidor degrada con gracia y declara la cobertura por resultado.
- Corpus total: **54 obras distintas, 11.724 páginas** (2.006 chat +
  6.340 Drive + 3.378 Biblioteca, conteo a 10 nov 2026; la Biblioteca
  creció a 24 obras el 24 nov 2026).

## Archivos

- `server.py` — servidor MCP (stdio + HTTP Streamable, stdlib).
- `renova_core.py` — corpus, política RNV-01..06, herramientas.
- `renova.py` + `renovar` — CLI / bot.
- `data/lucem.jsonl` — registro local de evidencia (se crea al usarlo).
- `TESTS.md` — resultados reales de cada prueba.
- `Dockerfile`, `requirements.txt` (vacío: solo stdlib), `configs/`.
