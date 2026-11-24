# Activación del MCP ℛenova — 2026-11-23

> Prototipo de laboratorio. CENTRO Guard no validado; veredictos
> simulados (DENY / REVIEW / ALLOW_SIMULATED), nunca ejecutan ni
> bloquean una acción real. Sin certificación ni validación externa,
> sin respaldo NIST/ISO/OWASP. **UNLICENSED (sin licencia): decisión
> pendiente de Rey; no añadir archivo de licencia.**

## Tabla de estado por plataforma

| Plataforma | Estado | Evidencia | Falta de Rey |
|---|---|---|---|
| **Muse (local)** | ✅ VERIFICADO | Servidor canónico stdlib corriendo: `http://127.0.0.1:8765`, PID 13790 (`server.pid`), `/health` → `{"status":"ok","server":"renova-mcp","version":"0.1.0"}`. Las 8 herramientas llamadas en vivo con `local_client.py` el 2026-11-23: search "CENTRO Guard" 27 resultados; documento `limites-declarados` íntegro verbatim; CENTRO publicar R3 sin autoridad → DENY (RNV-01); R-021 → DENY, gold null; transform propuesta; EGRA delta 4.0 simulado; LUCEM id `1f532a3583a6`, 5 entradas; get_state 54 obras / 11.724 págs. / 40 escenarios. CLI `./renovar` verificado. | Nada. Advertencia: es `nohup` en esta VM; un reinicio lo detiene y no hay arranque automático registrable desde esta sesión (ver fila «Persistencia local»). |
| **Unificación** | ✅ VERIFICADO | Implementación canónica única: stdlib 8 herramientas en `renova-mcp-server/`. La paralela FastMCP (6 herramientas) movida a `renova-mcp-server/archive-fastmcp/` (con su `.venv` y su `lucem_log.jsonl`, README de archivo). `custom.renova/CONNECTOR.md` actualizado: la canónica es la stdlib. | Nada. |
| **Vercel (despliegue público)** | ❌ NO — bloqueado por autenticación | Conector conectado, pero `list_projects` y `create_project` devuelven 403: `Not authorized: Trying to access resource under scope "seresarte"` (teamId `team_v4eM1DNE67lQHPpST8O7ONdH`). La API pide `authorize_team_access`, herramienta no disponible en el conector de Muse. Paquete listo y verificado en local: `vercel-deploy/` (13 MB, 45 archivos, `build.sh` + `api/mcp.py` + `api/health.py` + `vercel.json`); el servidor copiado responde `/health` y `tools/list` en puerto de prueba 8766. | Re-autenticar el acceso del equipo "seresarte" en Vercel (SSO del equipo) y reintentar. Ver `vercel-deploy/README-DEPLOY.md`. |
| **Replit (despliegue público, 2º intento)** | ❌ NO — falló | `create_app_from_prompt` (2026-11-23, prompt completo con las 8 herramientas, los 3 documentos fundacionales íntegros y las reglas RNV-01..06) devolvió: `phase: failed, error: http_error, errorMessage: "server returned status code Unauthorized"`, sin replId. No se creó ninguna app. | Nada que hacer desde aquí; la cuenta de Replit rechazó la creación. Reintentar desde replit.com o usar Vercel cuando se re-autentique. |
| **GitHub** | ✅ VERIFICADO — documentos y código | Repo creado 2026-11-23 20:23 CST; commit `79866df7` (2026-11-24T03:16:30Z, flujo paralelo) con docs, benchmark, canónicos y ROBOTS.md. Código del servidor MCP en `server/` del repo (paquete limpio, sin `.git/`, subido 2026-11-23 noche, commit `cbea99f03003a6b1a1a0ee4b4334a275921cc542`). Verificado por lectura del repo tras el push (`server/server.py` y `server/renova_core.py` presentes; README con sección «Servidor MCP»; puentes en `docs/bridges/`). | Nada. Si el push va por conector, añadir el repo a la instalación de la App de Muse (si aún no está). |
| **Drive** | ✅ VERIFICADO | Carpeta `RENOVA-MCP` (id `15AyWnegl8DmfImkD2hH74HV_coJGrh0h`), dentro de `11_BUS_3IA`, verificada por lectura el 2026-11-23: `shared: false` (privada), propietaria `c.jonathan.gr@gmail.com`. Contiene `renova-mcp-v0.1.0.zip` (id `1s9g7YnKRKhvVkB_0qAwRiiU-bnK0z079`), `renova-mcp-v0.1.0-limpio.zip` (paquete limpio, sin `.git/`, id `1baXDVUcUVafDvCP4otM_pFJ3hJw0iM9y`) y `STATUS-MCP-Renova.md` (id `1sV9DGfejeUs-EdKZaeD3RrHQUlrwScDA`). Puentes para ChatGPT/Grok/Gemini en OUTBOX del bus (CHATGPT-MCP.md `1Rh_rBEbCO4MLtRWut8cGmWCX8fdtOUy6`, GROK-BRIDGE.md `1eDZ8P4IHzk06GWap51Zw8WkI99Wt-DBg`, GEMINI-PACK.md `1QaZDdMB_a6AU6WpdKGx9JNYukWOgzQi1`, PROMPT-CORTO-MCP.md `1hy0C0SOWV4kwMH58eZAEelmvJv5yJ6tV`). Enlace: https://drive.google.com/drive/folders/15AyWnegl8DmfImkD2hH74HV_coJGrh0h | Nada. No se comparte en público. El local sigue siendo la fuente de verdad. |
| **Persistencia local** | ⚠️ SIN ARRANQUE AUTOMÁTICO | Servidor local corriendo en `127.0.0.1:8765` (nohup en esta VM). Arranque idempotente: `~/workspace/renova-mcp-server/start-server.sh`. No hay servicio systemd de usuario registrable desde esta sesión (`systemctl --user` → «Failed to connect to bus: No medium found»; `loginctl` → «Failed to connect to bus: No such file or directory») ni `crontab` en la máquina: tras un reinicio de la VM el servidor se detiene y hay que arrancarlo a mano con ese script (o pedirlo a Muse). | Nada que Muse pueda registrar solo; si el entorno ofrece un arranque al inicio, activarlo desde fuera de esta sesión. |
| **ChatGPT** | ❌ NO — sin enlace en vivo | Sin endpoint HTTPS público, no hay nada que conectar. Config plantilla en `configs/chatgpt_mcp_config.json` (URL de ejemplo `https://mcp.renova.example/mcp`, no existe). Instrucciones en `configs/README.md` y paquete para pegar en `~/workspace/renova-mcp-activation/CHATGPT-MCP.md`. | Esperar al despliegue público y conectar el MCP en ChatGPT (modo desarrollador) con su cuenta. |
| **Claude** | ⚠️ LOCAL SÍ / REMOTO NO | Local: `configs/claude_desktop_config.json` apunta al servidor stdio local (`server.py --stdio`) y funciona en una máquina con el repo. Remoto: sin endpoint público, no hay nada que conectar. | Para remoto, esperar al despliegue público. |
| **Grok / GrokBot** | ❌ NO — sin enlace directo | No hay cliente MCP nativo en Grok; grok.com bloquea a Muse; no hay API/MCP de GrokBot. Flujo por Rey como puente + continuidad en `BRIDGE-GROK-GEMINI.md` y paquetes en `~/workspace/renova-mcp-activation/GROK-BRIDGE.md`. | Rey pega los paquetes en su sesión de Grok; nada que conectar desde aquí. |
| **Gemini** | ❌ NO — sin conexión directa | Sin conector en Muse y sin cliente MCP directo. Paquete para pegar en `~/workspace/renova-mcp-activation/GEMINI-PACK.md`; flujo en `BRIDGE-GROK-GEMINI.md`. | Rey pega el paquete en su sesión de Gemini. |
| **Dependencias** | ✅ VERIFICADO | Canónico stdlib: cero dependencias (Python 3.12.3, `requirements.txt` vacío). `py_compile` OK en servidor, CLI y clientes. FastMCP archivado: venv propio con `mcp==1.12.0`. | Nada. |

## Licencia

**UNLICENSED.** No se añadió archivo de licencia en ningún sitio.
Decisión pendiente de Rey antes de cualquier publicación o
despliegue público con contenido.

## Qué se hizo en esta activación (2026-11-23)

1. Unificación: FastMCP archivada, una sola implementación canónica.
2. Servidor local arrancado (PID 13790) y 8/8 herramientas verificadas
   en vivo + `list-tools` + CLI `./renovar`.
3. Despliegue público intentado por dos vías, ambas bloqueadas por
   autenticación (Vercel 403 seresarte; Replit Unauthorized).
   Paquete Vercel listo y probado en local (`vercel-deploy/`, 13 MB).
4. Drive verificado (carpeta privada existente, con el zip v0.1.0);
   no se re-subió nada.
5. GitHub: repo creado por Rey/navegador; documentos + ROBOTS.md
   subidos por flujo paralelo (commit `79866df7`, 2026-11-24T03:16:30Z);
   código MCP subido 2026-11-23 noche con paquete limpio reconstruido
   sin `.git/` (commit `cbea99f03003a6b1a1a0ee4b4334a275921cc542`), verificado
   por lectura del repo. El paquete viejo `renova-mcp-push-ready/` no
   superó la revisión de riesgo de ejecución por llevar `.git/` con
   muestras de hooks; Rey ordenó «corrige en GitHub y monta todo» y
   delegó la decisión «hazlo lo más profesional»; el paquete viejo
   queda intacto como evidencia y no se copió su `.git/` a ningún lado.
6. Configs de Claude/ChatGPT actualizadas como "pendientes de
   endpoint"; puente Grok/Gemini documentado.
7. Nada publicado, nada pagado, nada escrito a terceros.

## Lo que solo Rey puede hacer

1. Re-autenticar Vercel (equipo seresarte) para el despliegue público.
2. Decidir la licencia.
3. Conectar ChatGPT/Claude al endpoint público cuando exista; pegar
   los paquetes en Grok/Gemini como puente.
