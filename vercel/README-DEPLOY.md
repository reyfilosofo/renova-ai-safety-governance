# Despliegue público del MCP ℛenova en Vercel

Paquete listo, verificado en local el 2026-11-23: `build.sh` lo ensambla
(13 MB, 45 archivos) y el servidor copiado responde `/health` y
`tools/list` con las 8 herramientas en el puerto de prueba 8766.

## Bloqueo actual (2026-11-23, verificado)

Vercel está conectado, pero todas las operaciones devuelven **403**:
`Not authorized: Trying to access resource under scope "seresarte"`.
TeamId: `team_v4eM1DNE67lQHPpST8O7ONdH`. La recuperación que pide la
propia API es `authorize_team_access` con ese teamId, herramienta que no
está en el conector de Muse. **Lo tiene que hacer Rey**: re-autenticar
el acceso del equipo "seresarte" en Vercel (SSO del equipo) y después
reintentar el despliegue. Sin ese paso no se puede crear proyecto ni
desplegar desde aquí.

## Cómo desplegar cuando el acceso esté re-autenticado

Opción A — con el conector de Muse (Vercel MCP):
1. `create_project` con `{"requestBody": {"name": "renova-mcp"}}`.
2. Subir los archivos con `upload_file` (uno por archivo; los 16 txt de
   `corpus/biblioteca/txt/` son los pesados) y luego `create_deployment`
   con `requestBody.files` referenciando cada `sha` + `size`.
3. Verificar la URL devuelta: `curl <url>/health` y un `initialize`
   contra `<url>/mcp`. Solo entonces la URL es real.

Opción B — con la CLI de Vercel, desde esta carpeta:
```bash
cd ~/workspace/renova-mcp-server/vercel-deploy
bash build.sh          # regenera corpus/ si cambió el canónico
vercel --scope seresarte   # o el equipo que corresponda
vercel deploy --prod
curl https://<url-asignada>/health
```

## Notas del despliegue serverless

- Sin estado: el servidor canónico no guarda sesiones en memoria, así
  que las funciones serverless funcionan (cada POST es independiente).
- LUCEM es efímero en Vercel (`/tmp/renova-data`): el registro durable
  sigue siendo el del servidor local (`renova-mcp-server/data/lucem.jsonl`).
- Sin autenticación todavía: el endpoint público no tiene OAuth. Los
  veredictos CENTRO siguen siendo simulados y el servidor no ejecuta
  ninguna acción real. OAuth queda pendiente de decidir con el hosting.
- `vercel.json` ya mapea `/mcp` → `/api/mcp` y `/health` → `/api/health`,
  con `maxDuration` 60 s en `/api/mcp`.

## Por qué el módulo se llama `renova_server.py` (2026-11-24)

Vercel detecta un `server.py` en la raíz del proyecto como entrypoint de
la aplicación y lo monta como función catch-all, por encima de `api/`.
El despliegue del 23 nov servía así solo `GET /` (el info de
`server.py`); `/health` y `/mcp` llegaban reescritos como `/api/health`
y `/api/mcp` al handler de `server.py`, que no los reconoce → 404
`{"error": "not found"}`. Por eso el servidor canónico se copia aquí
como `renova_server.py` (no es nombre de entrypoint) y `api/mcp.py` /
`api/health.py` lo importan así. No volver a poner un `server.py` en
esta raíz.

## Entrypoint WSGI `app.py` (2026-11-24)

Quitar `server.py` no bastó: sin entrypoint, Vercel no creó ninguna
función (ni siquiera las de `api/`) y todo pasó a 404, incluida `/`.
Según la documentación oficial, el preset Python de Vercel tiene
precedencia sobre las funciones de `api/` y carga un entrypoint
(`app.py`, `index.py`, `server.py`, `main.py`, `wsgi.py` o `asgi.py`)
que defina `app`. Por eso el entrypoint es ahora `app.py`, una app
WSGI stdlib que enruta todo ella misma (`/health`, `/`, `/mcp`, con
alias `/api/*` por tolerancia). Los wrappers de `api/` quedan como
respaldo si alguna vez no hay preset. No borrar `app.py` ni renombrar
`renova_server.py`.

## Ruta canónica del despliegue (A13, 2026-11-24)

- **Único entrypoint canónico: `app.py`** (WSGI stdlib). Es el que
  sirve `/health`, `/`, `/mcp` y los alias `/api/*` en producción.
- **`renova_server.py`** es la copia exacta del `server.py` canónico
  local (verificado por `diff` en cada sincronización); `app.py` lo
  importa como `renova_server` y reutiliza su `handle_request`.
- **`renova_core.py`** es la copia exacta del canónico local.
- **`api/mcp.py` y `api/health.py` son DUPLICADOS** del mismo endpoint
  (wrappers `BaseHTTPRequestHandler` alternativos, declarados además en
  `vercel.json` con `maxDuration`). No se borran todavía: su
  eliminación queda pendiente de la sincronización Vercel con
  verificación en vivo de que `app.py` es el handler que realmente
  responde (cada `/health` lleva `"handler": "app.py (WSGI)"` para
  distinguirlo; el local lleva `"handler": "server.py
  (BaseHTTPRequestHandler)"`). Hasta entonces, cualquier cambio de
  comportamiento debe hacerse en el canónico local y copiarse a
  `renova_server.py` / `renova_core.py`, no en `api/`.

## Sincronización 2026-11-24 ~00:15 CST (A1–A14 + Gemini H-01–H-10)

- Código corregido subido a `vercel/`: `renova_server.py` (copia exacta
  de `server.py` canónico, `diff` idéntico), `renova_core.py` (copia
  exacta del canónico), `app.py` (H-01: `RENOVA_PUBLIC_ENDPOINT=1`,
  H-06: `"handler": "app.py (WSGI)"` en `/health`, A14: 415,
  A1: 413 antes de leer + rate limit 60/min por IP → 429, 202 con
  cuerpo `{}`), `vercel.json`, `build.sh`, `README-DEPLOY.md`.
- **A13 ejecutada:** `api/mcp.py` y `api/health.py` eliminados de
  `vercel-deploy/`, de `vercel.json` (solo queda `app.py`,
  `maxDuration` 60) y del repo `vercel/api/` (borrado por conector).
  `app.py` es el ÚNICO entrypoint y enruta `/mcp`, `/api/mcp`,
  `/health`, `/api/health` (verificado en local con wsgiref sin que
  existan los archivos `api/*.py`, antes del push). Las rewrites
  `/mcp`→`/api/mcp` y `/health`→`/api/health` se mantienen.
- **Libro 04 por partes:** el txt único de 6.8 MB NO se sube (da 413
  en el conector). En el repo ya estaban las 5 partes
  `04_renova_H_v74.part1-5.txt` (~1.37 MB cada una, commits
  57f0aa5d/d70e2aeb/c5186c7d) y `renova_core.py` las lee como un solo
  texto (`<stem>.partN.txt`); `renova_search` devuelve la obra 04 con
  933,922 palabras. El paquete local se alineó: partes copiadas,
  txt único eliminado del paquete (el original sigue en
  `~/workspace/renova-biblioteca-2026-11-10/txt/`).
- **Biblioteca 17–24:** obras nuevas subidas por Rey el 24 nov
  (Burbuja Comercial, Essentiae Crítica, Qualia Quanta Ser, Burbuja
  Definitiva, Renova V10, Essentiae Final, Qualia Renovativos,
  Campayo Renovativo) añadidas a `vercel/corpus/biblioteca/txt/`;
  `get_state` pasa a 24 obras (23 indexadas, 1 solo metadatos).
- Commits de esta sincronización: (ver reporte de sincronización).
- Verificación en vivo tras el auto-redeploy: `/health` 200 con
  `"handler": "app.py (WSGI)"`, `initialize` 200, `tools/list` 8,
  `get_state` con claves nuevas, búsqueda obra 04 (933,922 palabras),
  CENTRO publicar sin autoridad → DENY RNV-01, `renova_lucem_log` →
  error controlado (escritura desactivada en el endpoint público).

## Pendientes

- Licencia: Apache 2.0 para código y documentación del servidor MCP
  (LICENSE + NOTICE, commit 5c14792a, decisión de Rey 2026-11-24
  00:10); textos completos del corpus con todos los derechos
  reservados. `renova_get_state` aún reporta UNLICENSED en el código
  de esta sincronización; actualizar esa cadena queda fuera del
  alcance de esta tarea (hilo de licencia).
- Sin OAuth en el endpoint público (decisión explícita; ver A1/H-01).
- `build.sh` regenera `corpus/` desde las fuentes canónicas y vuelve a
  copiar el txt único de la obra 04 (6.8 MB): antes de volver a usarlo
  hay que partir la obra 04 en `.partN.txt` o excluirla del copiado.
- Sin `deployment_commit` en `get_state` (pendiente).
