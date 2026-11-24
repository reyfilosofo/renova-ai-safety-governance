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
