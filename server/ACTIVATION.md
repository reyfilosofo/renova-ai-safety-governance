# Activación del MCP ℛenova — actualización 2026-11-24 (autocorrección recursiva)

> Prototipo de laboratorio. CENTRO Guard no validado; veredictos
> simulados (DENY / REVIEW / ALLOW_SIMULATED), nunca ejecutan ni
> bloquean una acción real. Sin certificación ni validación externa,
> sin respaldo NIST/ISO/OWASP.
>
> **Licencia:** el repo tiene `LICENSE` Apache 2.0 + `NOTICE` desde
> 2026-11-24 00:10 CST (commit `5c14792a`, decisión de Rey). Alcance:
> cubre el código del servidor MCP (`server/`, `vercel/` sin el
> corpus) y la documentación del programa; los textos completos de
> las obras del corpus (`vercel/corpus/`) NO quedan bajo esta
> licencia: son obras del autor con todos los derechos reservados.
> **Divergencia conocida (actualizada en el hilo de licencia,
> 2026-11-24 ~00:20 CST):** la cadena `UNLICENSED` del canónico
> local ya está actualizada a `Apache-2.0` (`renova_core.py`:
> docstring, lista `LIMITS` y `renova_get_state`; verificado por
> stdio: `license: Apache-2.0`). La copia `vercel-deploy/renova_core.py`
> y el endpoint en vivo siguen reportando UNLICENSED hasta la próxima
> sincronización + redespliegue; el servicio local en ejecución
> (PID 2655) lo refleja tras su próximo reinicio.

## Tabla de estado por plataforma

| Plataforma | Estado | Evidencia | Falta |
|---|---|---|---|
| **Muse (local)** | ✅ VERIFICADO | Servidor canónico stdlib en `http://127.0.0.1:8765`, `/health` → 200 `{"status":"ok","handler":"server.py (BaseHTTPRequestHandler)",...}` con las 8 herramientas. Reiniciado 2026-11-24 ~00:18 CST tras un reemplazo de VM (ver «Incidentes»): PID 2655, `renova_get_state` → `prototipo_de_laboratorio`, `degraded false`, `warnings []`, staging 16 docs, biblioteca 24 obras / 4.478 págs. / 1.869.502 palabras, indexadas 23, solo metadatos 1, fundamento 54/11.724 (declarados, ver A3), benchmark 40 escenarios, author labels 8 ALLOW_SIMULATED / 17 DENY / 15 REVIEW, gold_label null. Código corregido (ronda A1–A14/H-01–H-10, ver abajo) y probado en local. CLI `./renovar` verificado. | Nada. |
| **Vercel (despliegue público)** | ✅ VERIFICADO — en vivo, código corregido | **https://renova-mcp.vercel.app** (proyecto `renova-mcp`, equipo seresarte, repo `reyfilosofo/renova-ai-safety-governance`, Root Directory `vercel/`, Deployment Protection desactivada). Sincronizado 2026-11-24 ~00:14 CST con el código corregido (commits `926953c8` + `6d2dd959`, ver «Sincronización Vercel»). Verificado en vivo: `GET /health` y `/api/health` → 200 con `"handler": "app.py (WSGI)"`; `POST /mcp` initialize → 200, `protocolVersion 2025-11-25`; `tools/list` → 8 herramientas; `renova_get_state` → prototipo, `degraded false`, staging 16, biblioteca 24 obras en metadatos pero **indexadas 15 / solo metadatos 9** (obras 17–24 aún no en el repo: push denegado, ver pendientes), 1.620.676 palabras; `renova_search "Habitat Herida Horizonte"` → obra 04, 933.922 palabras; CENTRO publicar sin autoridad → DENY RNV-01; `renova_lucem_log` → isError (desactivado en público); benchmark 10/10 HTTP 200. LUCEM efímero en `/tmp`; sin OAuth (decisión documentada, ver A1/H-01). | Aprobar el push de las obras 17–24 y el borrado de `vercel/api/health.py` (ver pendientes). |
| **GitHub** | ✅ VERIFICADO | Repo `reyfilosofo/renova-ai-safety-governance`, público. Commits recientes: `cbea99f0` (código MCP en `server/`, paquete limpio), `79866df7` (documentos), `9d424fa1` (puentes revisados por Gemini), `ad6e70aa` (bitácora de auditoría en `docs/`), `5c14792a` (LICENSE Apache 2.0 + NOTICE), `926953c8` (código corregido en `vercel/`), `6d2dd959` (borrado de `vercel/api/mcp.py`). **Divergencia conocida:** `server/` del repo aún contiene el código previo a la corrección (commit `cbea99f0`, 585 líneas, sin los marcadores de la corrección); el código corregido está en local y en `vercel/`. Sincronizar `server/` queda pendiente (no se pusheó en esta ronda). | Sincronizar `server/` con el canónico local corregido. |
| **Drive** | ✅ VERIFICADO | Carpeta `RENOVA-MCP` (id `15AyWnegl8DmfImkD2hH74HV_coJGrh0h`), dentro de `11_BUS_3IA`, privada, propietaria `c.jonathan.gr@gmail.com`. Contiene `renova-mcp-v0.1.0.zip` (id `1s9g7YnKRKhvVkB_0qAwRiiU-bnK0z079`), `renova-mcp-v0.1.0-limpio.zip` (id `1baXDVUcUVafDvCP4otM_pFJ3hJw0iM9y`) y `STATUS-MCP-Renova.md` (id `1sV9DGfejeUs-EdKZaeD3RrHQUlrwScDA`). Puentes corregidos actualizados **en su sitio** en OUTBOX del bus y verificados por md5 tras la descarga: CHATGPT-MCP.md `1Rh_rBEbCO4MLtRWut8cGmWCX8fdtOUy6`, GROK-BRIDGE.md `1eDZ8P4IHzk06GWap51Zw8WkI99Wt-DBg`, GEMINI-PACK.md `1QaZDdMB_a6AU6WpdKGx9JNYukWOgzQi1` (ahora md5 `65d26ff5…`, 3.994 bytes), PROMPT-CORTO-MCP.md `1hy0C0SOWV4kwMH58eZAEelmvJv5yJ6tV` (ahora md5 `572845df…`, 2.156 bytes). Enlace: https://drive.google.com/drive/folders/15AyWnegl8DmfImkD2hH74HV_coJGrh0h | Nada. No se comparte en público. El local sigue siendo la fuente de verdad. |
| **ChatGPT** | ✅ CONECTADO 2026-11-23 23:21 | Complemento «Renova MCP» en ChatGPT (Settings → Integrations → Plugins), URL https://renova-mcp.vercel.app/mcp, sin autenticación, 8 herramientas. Prueba en chat: `renova_get_state` devolvió el JSON exacto del servidor. Cuenta SERESARTE (c.jonathan.gr@gmail.com, Plus). Detalle: https://chatgpt.com/plugins/plugin_asdk_app_6b051e6182c481918ff77da3adf08692 | Nada. |
| **Grok** | ✅ CONECTADO 2026-11-23 23:28 | Conector personalizado «Renova MCP» en grok.com (Conectores → Add a custom connector), URL https://renova-mcp.vercel.app/mcp, sin OAuth, 8 herramientas, estado «Connected», «Todas las herramientas activadas». Conectores 24 → 25. Esto corrige la afirmación anterior «Grok no tiene MCP directo»: sí tiene interfaz de conector MCP personalizado. `GROK_BOT_ENDPOINT` sigue sin existir; no inventarlo. | Nada. Verificación pendiente: si Grok Bot (ℝ𝔼𝕐) comparte este conector. |
| **Gemini** | ✅ CONECTADO 2026-11-23 23:51 | Vía Antigravity CLI (`agy` 1.5.16): servidor `renova` registrado (`agy mcp add renova https://renova-mcp.vercel.app/mcp`), OAuth con Google completado 23:50, token en `~/.gemini/antigravity-cli/antigravity-oauth-token`. Verificado en vivo 23:51: `agy -p` llamó `renova_get_state` y devolvió «renova-mcp v0.1.0, prototipo_de_laboratorio». La web de Gemini NO tiene forma de añadir un MCP personalizado (verificado 23:36, catálogo cerrado); el relevo de secretaría sigue por el chat web «Relevo de Secretaría y MCP ℛenova». En modo no interactivo las herramientas MCP arrancan en modo «ask»: hace falta una regla de permiso o `--dangerously-skip-permissions`. | Nada. Ruta opcional SDK + clave gratuita de AI Studio sigue disponible si se quiere (no necesaria: el CLI ya está conectado). |
| **Claude** | ✅ CONECTADO 2026-11-24 00:04 | Rey inició sesión en claude.ai con su Google; conector personalizado «Renova MCP» (https://renova-mcp.vercel.app/mcp, sin autenticación), estado Agregado y Conectado, 8 herramientas, plan Free, sin pagar nada. | Nada. |
| **Persistencia local** | ⚠️ SUPERVISADO — sin arranque automático tras reemplazo de VM | Unidad systemd `renova-mcp.service` (Restart=always) creada 2026-11-23 22:15 con copia canónica en `~/workspace/renova-mcp-server/renova-mcp.service`. **El reemplazo de VM de 2026-11-24 ~00:16 borró `/etc`**: la unidad y el drop-in `home.conf` desaparecieron y el servidor quedó abajo; se rearrancó a mano con `start-server.sh` (ver «Incidentes»). Vigía `renova-mcp-watchdog` cada 30 min: si /health falla, reinicia con `start-server.sh` (idempotente). No hay bus systemd de usuario ni `crontab` en la máquina. | Nada que Muse pueda registrar solo; si el entorno ofrece un arranque al inicio, activarlo desde fuera de esta sesión. Tras un reemplazo de VM hay que reinstalar la unidad (o rearrancar con `start-server.sh`). |
| **Replit (despliegue público, 2º intento)** | ❌ NO — falló | `create_app_from_prompt` (2026-11-23) devolvió `phase: failed, error: http_error, errorMessage: "server returned status code Unauthorized"`, sin replId. No se creó ninguna app. | Nada que hacer desde aquí; la cuenta de Replit rechazó la creación. |
| **Dependencias** | ✅ VERIFICADO | Canónico stdlib: cero dependencias (Python 3.12.3, `requirements.txt` vacío). `py_compile` OK en servidor, CLI y clientes. FastMCP archivado: venv propio con `mcp==1.12.0`. | Nada. |

## Autocorrección recursiva (2026-11-23 23:54 → 2026-11-24 00:04, verificada en local)

Orden de Rey: «Corrige a ti mismo, sé recursivo y autónomo y agéntico».
Trabajo en local y en el repo; sin navegador, sin publicar nada nuevo,
sin pagar nada, sin escribir a terceros. Sin cambios de nombres de
herramientas ni del contrato de la API. Hallazgos del brief
(AUDITORIA-BRIEF-GEMINI.md, A1–A16) y de la auditoría de Gemini
(AUDITORIA-GEMINI-2026-11-23.md, H-01–H-10).

| Hallazgo | Corrección aplicada | Evidencia |
|---|---|---|
| A8 / H-03 — EGRA pesos todos 0 | `ZeroDivisionError` eliminado: pesos todos 0 → `{"status": "sin_pesos_validos"}` sin inventar medias; peso negativo → `ValueError` (isError). Un solo peso 0 permitido (documentado). | Suite local: EGRA 0 → `sin_pesos_validos`; EGRA −1 → isError. |
| A4 — cardinalidad | `parse_policy`/`parse_benchmark` exigen exactamente 6 políticas RNV-01..RNV-06 y 40 escenarios R-001..R-040; si no cuadra, el servidor falla en el arranque con `RuntimeError` y mensaje claro. `tool_centro_evaluate` se niega con política vacía (`ValueError`). | Pruebas: 5 políticas / RNV-99 / 39 escenarios → `RuntimeError` en arranque. |
| A5 — arranque degradado | Inventario JSON corrupto o staging vacío ya no tumban el arranque ni degradan en silencio: arranque en modo degradado con advertencias visibles en `CORPUS.warnings`, `get_state` (`degraded`/`warnings`) y stderr. Staging con contenido pero sin política/benchmark válidos → fallo duro (A4). | Prueba: inventario corrupto + staging vacío → `degraded True`, 4 advertencias. |
| A7 / H-07 — rutas absolutas | Ninguna respuesta de herramienta incluye rutas absolutas: `tool_search`/`tool_get_document` sin `"path"`; `tool_lucem_log` devuelve solo `"lucem.jsonl"`; `parse_policy` usa `"centro-guard-policy.yaml"`. | Verificado: ninguna respuesta contiene `/home/hatch` ni `/tmp/` ni `/var/task/`. |
| A1 / H-01 — endurecimiento (parcial, sin auth) | Cuerpo >1 MB → 413 antes de `.read()`; 60 req/min/IP → 429; `BoundedSemaphore(8)` → 503 (server.py). `renova_lucem_log` **desactivado en el endpoint público** (`RENOVA_PUBLIC_ENDPOINT=1`, fijado por app.py): devuelve error con isError y no escribe nada (ni siquiera crea el directorio). Hilos acotados (max_workers=8). **Decisión documentada: NO se añade autenticación ni OAuth al endpoint público** — rompería las conexiones ya verificadas de ChatGPT (23:21), Grok (23:28), Gemini/Antigravity CLI (23:51) y Claude (00:04). La escritura pública es el riesgo, y se cierra restringiéndola en remoto; la decisión de un esquema de autenticación sigue siendo de Rey. | HTTP 8766: cuerpo >1 MB → 413; 61 rápidas → 57×200 + 4×429; WSGI: lucem público → isError. En vivo: `renova_lucem_log` → isError «desactivado en el endpoint publico». |
| A3 / H-05 — conteos 54/11724 | No derivables del inventario (sus `conteos` dan una unión 38/39 obras, sin páginas por obra en Drive; las sumas del chat dan 2.006). Se mantienen como **valores declarados** con `fundamento_counts_source` («metadatos verificados 2026-11-10…; valores declarados, no calculados del texto»). Claves nuevas `biblioteca_works_indexed` / `biblioteca_works_metadata_only` / `biblioteca_works_with_text`; las claves viejas se mantienen como alias. Sin `deployment_commit`. | `get_state` local: fundamento 54/11724 con `fundamento_counts_source` presente; indexadas 23 / solo metadatos 1. |
| A10 / H-09 — conformidad MCP | params/arguments no-dict → −32602 (no −32603); `prompts/get` con arguments null → `{}`; versión desconocida negocia 2025-11-25 + advertencia en stderr; `Accept` solo advertencia (nunca se rechaza); lote (array) → −32600, documentado en README. | Suite: versión desconocida → 2025-11-25; params no-dict → −32602; lote → −32600. |
| A14 — Content-Type | Content-Type presente y ≠ application/json (charset permitido) → 415; ausente → aceptado. | Socket crudo: CT text/plain → 415; ausente → 200. |
| A9 — RNV-05 | Documentado en el docstring de `tool_centro_evaluate`, en el detalle de RNV-05 y en el README: RNV-05 exige `human_approval` incluso para lecturas R0. El caso «leer → ALLOW» solo funciona con `human_approval=true`. TESTS.md §2 prueba 6 corregida. | CLI `evaluate` con los flags nuevos → RNV-03/RNV-05 PASS, REVIEW; sin `--affected-approval` → DENY RNV-03. |
| A11 / H-10 — transform | «no verificado» / «sin verificar» ya no cuentan como positivo (negaciones primero + lookbehind `(?<!no\s)verificado`); «Dato verificado.» sigue positivo. `authority_identity` sanitizada (sin `[\r\n\t]` ni controles, truncada a 200). | Pruebas locales de transform. |
| A12 / H-08 — CLI | `renovar evaluate` con `--affected-approval` y `--human-approval-specific` (`--human-approval` implica specific si no se pasa el flag); `compare` con JSON inválido → mensaje claro, salida 1, sin traceback. | CLI verificado. |
| A13 / H-06 — handlers Vercel | Una sola ruta canónica documentada: `app.py` es el único entrypoint; `api/mcp.py` y `api/health.py` eliminados de `vercel-deploy/` y de `vercel.json` (solo `app.py`, maxDuration 60). `api/mcp.py` borrado del repo (commit `6d2dd959`); el borrado de `api/health.py` fue denegado por el usuario y sigue en el repo, pero **no interfiere**: responde `app.py` (precedencia del entrypoint). `/health` incluye `"handler"` (`server.py (BaseHTTPRequestHandler)` en local, `app.py (WSGI)` en Vercel) para verificar en vivo qué código responde. `/health` 202 con cuerpo `{}` como server.py. | Prueba local con wsgiref sin `api/` antes del push: todas las rutas 200; en vivo `/health` → `"handler": "app.py (WSGI)"`. |
| H-02 — política vs código | `POLICY_RULE_IDS` es la única fuente de verdad; `parse_policy` y `Corpus.__init__` verifican la coincidencia exacta entre el código y la política cargada. RNV-99 en vez de RNV-06 → `RuntimeError` en arranque. | Prueba de arranque con RNV-99 → `RuntimeError`. |
| H-04 — LUCEM | Lock global `threading.Lock()` + `fcntl.flock` exclusivo (lectura y escritura sobre el mismo descriptor `a+`), flush + fsync; cola corrupta → `chain_reset_reason="corrupt_tail"` registrado (nada de reiniciar `prev_hash` en silencio). Limitación documentada: solo se valida la cola. | Prueba concurrente: 10 hilos → cadena lineal; cola corrupta → `chain_reset_reason="corrupt_tail"`. `data/lucem.jsonl` de producción intacto (91 líneas; las pruebas usaron un `RENOVA_DATA_DIR` temporal). |
| H-03 — Content-Length | Content-Length no numérico en server.py → 400 sin matar el hilo. | Prueba: Content-Length `abc` → 400 y servidor vivo. |
| A2 — libro 04 | La obra 04 (`04_renova_H_v74.txt`, 6,8 MB) no se puede subir por el conector (413): se partió en 5 partes `part1–5.txt` (SHA256 concatenado idéntico al original, 933.922 palabras) y `renova_core.py` lee `<stem>.partN.txt`. Commits `c0f2de38`, `57f0aa5d`/`d70e2aeb`/`c5186c7d` (partes), `5d6d8691` (server/). El archivo único de 6,8 MB no debe reintentarse nunca. | En vivo: `renova_search "Habitat Herida Horizonte"` → obra 04, 933.922 palabras; `biblioteca_16_words` 1.620.676. |
| A15 — búsqueda | Revisado en esta ronda; sin cambio de comportamiento registrado. | — |
| A16 — deriva de despliegue | Sincronización Vercel completada (ver sección siguiente); `get_state` en vivo ya devuelve las claves nuevas (`biblioteca_works`, `biblioteca_works_indexed`, `fundamento_counts_source`). | En vivo 2026-11-24 ~00:14 CST. |

Pruebas locales tras la corrección (TESTS.md §10): `py_compile` OK;
stdio 16 llamadas rc 0 (search «CENTRO Guard» total 35, antes 27 con la
biblioteca ampliada; R-021 DENY/gold null; EGRA delta 1.67) + casos nuevos;
HTTP 8766 y WSGI app.py (415/413/429/400/lucem bloqueado); modo degradado;
LUCEM concurrente; CLI. Libro 04 intacto en el servicio reiniciado.

## Sincronización Vercel (A16 + A2) — 2026-11-24 ~00:05–00:14 CST

Inventario previo por blob SHA entre `vercel-deploy/` local y `vercel/`
del repo: `vercel.json` idéntico; `app.py`, `renova_server.py`,
`renova_core.py` y `README-DEPLOY.md` desactualizados; `api/*.py`
duplicados; staging y corpus 01–03/05–16 idénticos; obra 04 en partes ya
en el repo; obras 17–24 faltaban en el repo y en `vercel-deploy/`
(fuente: `~/workspace/renova-biblioteca-2026-11-10/txt/`).

- **Tanda 1 — código, commit `926953c874a9e2181dbdc5215449e1b75c628ed9`**
  (~75 KB): `vercel/renova_server.py`, `renova_core.py`, `app.py`,
  `vercel.json`, `README-DEPLOY.md`, `build.sh`. Verificado tras el
  push: 6/6 idénticos por blob SHA. `diff` canónico verificado:
  `vercel-deploy/renova_server.py` == `server.py`,
  `renova_core.py` == canónico.
- **Borrado `vercel/api/mcp.py` del repo, commit `6d2dd959`.**
- **Tanda 2 — corpus 17–24: DENEGADA por el usuario en el prompt de
  aprobación. No reintentada.** Tampoco se pudo borrar
  `vercel/api/health.py` del repo: **denegado por el usuario**
  (no reintentado). Ambas denegaciones quedaron anotadas en el README
  local. Los txt de 17–24 ya están copiados y verificados por hash en
  `vercel-deploy/` y en `vercel-push-staging/vercel/` (listos para
  re-push, ~2,1 MB en una tanda).
- Auto-redeploy <2 min (push ~06:13 UTC; `/health` nuevo ya a las
  06:14:43 UTC). Verificación en vivo completa en la fila «Vercel» y
  benchmark 10/10 HTTP 200 (`run-benchmark-calls.sh`, resultados en
  `resultados-benchmark-2026-11-23.json`; única deriva: `get_state`
  esperaba `biblioteca_works 16` —expectativa vieja del JSON— y da
  `24` / 1.620.676 palabras, correcto para el código nuevo con corpus
  incompleto; resto exacto: R-001 ALLOW_SIMULATED, R-010 DENY, R-021
  DENY, R-040 ALLOW_SIMULATED, todos `gold_label null`; centro
  publicar DENY RNV-01; centro leer ALLOW_SIMULATED; search CENTRO
  Guard total 27).
- Durante el trabajo el head avanzó por otros hilos: `ad6e70aa`
  (bitácora Gemini) y `5c14792a` (LICENSE Apache 2.0 + NOTICE). Las
  rutas no colisionaron; los blobs se re-verificaron antes de pushear.

## Puentes corregidos (Frente 2) — repo + Drive

- Primer push, commit **`d3bce4a452f3cb91faae55e09c319097d61ed4ad`**
  (4 archivos de PUENTES-CORREGIDOS/, con la actualización Gemini CLI
  23:51): repo `docs/bridges/` verificado por relectura
  (CHATGPT-MCP.md blob `12de5315…`, 3.436 bytes; GROK-BRIDGE.md
  `a027c74f…`, 3.186 bytes; GEMINI-PACK.md `49c3052a…`, 4.275 bytes;
  PROMPT-CORTO-MCP.md `28dd93ac…`, 2.397 bytes); Drive OUTBOX
  actualizado en su sitio (mismos ids) con md5 verificado por descarga.
- Reconciliación (revisión Frente 2 de Gemini), commit
  **`9d424fa16aaf35477b295c474393760f8e2bcaf7`**: solo GEMINI-PACK.md
  (blob `fe7553b9…`, md5 `65d26ff505e9741182de44195ae4c363`) y
  PROMPT-CORTO-MCP.md (blob `13fb2b00…`, md5
  `572845df936e6b1b2db057daa08068dc`). CHATGPT-MCP.md y GROK-BRIDGE.md
  intactos (Gemini los encontró exactos). Drive actualizado en su
  sitio y verificado por md5 (ver fila «Drive»).
- Bitácora consolidada de Gemini (tres frentes) subida a
  `docs/BITACORA-AUDITORIA-MCP-2026-11-23.md`, commit
  `ad6e70aadc083ded4eae42d14354f0d7cf6f3f62`, verificada por relectura
  (md5 `86492128f430156744f145e7a65d5205`, idéntico al local).

## Incidentes

1. **Reinicio degradado (2026-11-24 ~00:04 CST).** El primer
   `systemctl restart` tras la corrección arrancó degradado (staging 0,
   biblioteca 0). Causa: la unidad corre como root sin `HOME`, así que
   `Path.home()` resolvía a `/root` y el corpus quedaba vacío — el
   código viejo lo servía vacío **en silencio**; A5 lo hizo visible.
   No hay usuario `hatch` en la VM (root con `HOME=/home/hatch`).
   Corrección reversible sin tocar la unidad: drop-in
   `/etc/systemd/system/renova-mcp.service.d/home.conf` con
   `Environment=HOME=/home/hatch` + `daemon-reload` + restart.
   Verificación final entonces: `/health` 200, `get_state` prototipo,
   degraded False, staging 16, biblioteca 24/4478/1.869.502, indexadas
   23, fundamento 54/11724, benchmark 40, políticas RNV-01..RNV-06.
2. **Reemplazo de VM (2026-11-24 ~00:16 CST).** `/etc` no persiste:
   la unidad `renova-mcp.service` y el drop-in `home.conf`
   desaparecieron y el servidor quedó abajo (sin proceso, `server.pid`
   obsoleto 4258). Además `start-server.sh` había perdido el bit de
   ejecución (modo `-rw-rw----`, reescrito en la ronda de corrección).
   Se restauró el bit (`chmod +x`) y se rearrancó con el script:
   PID 2655, `/health` 200, `get_state` degraded False (ver fila
   «Muse (local)»). El vigía `renova-mcp-watchdog` (cada 30 min)
   debería haberlo rearrancado solo; el servidor estaba abajo cuando
   se comprobó a las ~00:18, así que el vigía no había actuado aún o
   no se disparó tras el reemplazo. Tras un reemplazo de VM hay que
   reinstalar la unidad (o rearrancar con `start-server.sh`).

## Lo que queda pendiente

1. **`server/` del repo con el código previo a la corrección**
   (commit `cbea99f0`): sincronizar con el canónico local corregido y
   probado. No se pusheó en esta ronda.
2. **Obras 17–24 en `vercel/corpus/biblioteca/txt/`**: push denegado
   por el usuario; requiere aprobación explícita nueva. Sin esto,
   `get_state` en vivo seguirá en indexadas 15 / solo metadatos 9
   (1.620.676 palabras en vez de 1.869.502; diferencia 248.826, justo
   las 8 obras).
3. **Borrar `vercel/api/health.py` del repo**: borrado denegado por el
   usuario; el archivo viejo sigue en el repo (SHA `246f29c2`). Hoy no
   interfiere (responde `app.py`), pero A13 queda incompleta hasta
   borrarlo con aprobación explícita.
4. **`get_state` y la cadena de licencia:** el canónico local ya
   reporta `"license": "Apache-2.0"` (actualizado en el hilo de
   licencia, 2026-11-24 ~00:20 CST, verificado por stdio). Pendiente:
   sincronizar `vercel-deploy/renova_core.py` + `server/` del repo y
   redesplegar para que el endpoint en vivo deje de reportar
   UNLICENSED; el servicio local en ejecución lo refleja tras su
   próximo reinicio.
5. `deployment_commit` no añadido a `get_state` (decisión pendiente).
6. LUCEM solo valida la cola (tail); sin auth global en el endpoint
   público (decisión explícita, ver A1/H-01).
7. `README-DEPLOY.md` con la nota de denegación y la verificación
   final solo está en local; `build.sh` regenera `corpus/` copiando el
   txt único de la obra 04 (6,8 MB): antes de volver a usarlo hay que
   partir la obra 04 en `.partN.txt` o excluirla (anotado en el README
   local).
8. Benchmark ℛ: revisión ciega pendiente (gold_label null en los 40);
   CENTRO-001 sin ejecutar (preregistro sin umbrales ni personas).

## Qué se hizo en esta ronda (2026-11-23/24)

1. Corrección recursiva del código canónico (A1–A16, H-01–H-10) con
   pruebas locales después de cada cambio; nada revertido por fallo de
   pruebas. Copias sincronizadas por diff idéntico:
   `vercel-deploy/renova_server.py` ← `server.py`,
   `vercel-deploy/renova_core.py` ← `renova_core.py`.
2. Sincronización de Vercel con el código corregido + verificación en
   vivo completa + benchmark 10/10.
3. Puentes corregidos en repo `docs/bridges/` y en Drive OUTBOX
   (mismos ids, md5 verificados); bitácora de Gemini en `docs/`.
4. Conexiones verificadas: ChatGPT 23:21, Grok 23:28, Gemini/Antigravity
   CLI 23:51, Claude 00:04. Libro 04 resuelto en 5 partes (933.922
   palabras, verificado en vivo).
5. Servidor local rearrancado tras el reemplazo de VM (PID 2655,
   sano, no degradado).
6. Licencia decidida por Rey: Apache 2.0 (commit `5c14792a`).
7. Nada publicado a terceros, nada pagado, nada escrito a terceros,
   sin auth/OAuth añadido, sin cambios de nombres de herramientas ni
   del contrato de la API.

## Lo que solo Rey puede hacer

1. Aprobar el re-push de las obras 17–24 a `vercel/corpus/` (tanda
   lista, ~2,1 MB).
2. Aprobar el borrado de `vercel/api/health.py` del repo.
3. Verificar su número de teléfono en YouTube Studio (miniatura
   personalizada y comentario fijado esperan eso) — fuera del MCP,
   se deja aquí porque sigue pendiente en el ecosistema.
