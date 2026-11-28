# Pruebas del servidor MCP ℛenova — resultados reales

Fecha: 2026-11-23. Servidor: `renova-mcp-server/` v0.1.0 (stdlib, sin
dependencias). Nada de lo aquí anotado es una prueba en público ni una
validación externa: son llamadas locales contra los archivos canónicos.

## Nota de actualización — 27 de noviembre de 2026

Este archivo es un registro fechado de pruebas locales (fecha: 2026-11-23,
con ampliaciones fechadas en las secciones 8–11). Nada de lo que sigue se
reescribe: lo que cambió después se anota aquí, con su fecha.

- **Licencia:** las menciones a «UNLICENSED» en este archivo (§7 y §10)
  describen el estado del 23–24 nov 2026, cuando la licencia estaba
  pendiente de decisión de Rey. La decisión se tomó el 24 nov 2026:
  **Apache 2.0** para el código y la documentación del servidor MCP
  (commit `5c14792a`, `LICENSE` + `NOTICE` en el repo;
  `server/UNLICENSED.txt` eliminado del repo). Los textos completos de
  las obras del corpus siguen con todos los derechos reservados.
- **Despliegue remoto:** lo que §7 dice del despliegue remoto («solo
  instrucciones», endpoint de ejemplo `https://mcp.renova.example/mcp`
  inexistente) era el estado del 23 nov 2026 antes de las 23:11 CST. El
  endpoint público **https://renova-mcp.vercel.app/mcp está en vivo desde
  el 23 nov 2026, 23:11 CST**; `renova_get_state` verificado en vivo el
  27 nov 2026: `deployment_commit` = HEAD del repo (`c6dd33b1`), licencia
  Apache-2.0, 8 herramientas. El endpoint de ejemplo de §7 sigue sin
  existir; el endpoint real es el de Vercel.

## 1. Compilación

```text
python3 -m py_compile renova_core.py server.py renova.py \
  ~/workspace/custom-connectors/custom.renova/bin/local_client.py \
  ~/workspace/custom-connectors/custom.renova/bin/mcp_client.py
COMPILE-ALL-OK
```

## 2. stdio (`/tmp/test_stdio.py`, 16 llamadas)

| # | Llamada | Resultado real |
|---|---|---|
| 1 | `initialize` | `protocolVersion=2025-06-18`, server `renova-mcp 0.1.0` |
| 2 | `tools/list` | 8 herramientas: renova_search, renova_get_document, renova_centro_evaluate, renova_benchmark_scenario, renova_transform, renova_egra_compare, renova_lucem_log, renova_get_state |
| 3 | `renova_search` "CENTRO Guard" | `total: 27`, isError=False |
| 4 | `renova_get_document` limites-declarados | 67 palabras, isError=False |
| 5 | `renova_centro_evaluate` publicar, R3, sin autoridad, evidencia Faltante | **DENY** |
| 6 | `renova_centro_evaluate` leer, R0, autoridad verificada, evidencia Confirmada, `human_approval=true` | **ALLOW_SIMULATED** (RNV-05 exige aprobación humana incluso para lecturas R0: sin `human_approval=true` el mismo caso da REVIEW) |
| 7 | `renova_benchmark_scenario` R-021 | author_label DENY, gold_label null |
| 8 | `renova_transform` "La IA siempre tiene la razon..." | status propuesta_no_validacion, 10 palabras |
| 9 | `renova_egra_compare` con puntuaciones | simulado, verdict tratamiento_supera_baseline, delta 1.67 |
| 10 | `renova_egra_compare` sin puntuaciones | **incompleto_sin_datos** (no inventa puntuaciones) |
| 11 | `renova_lucem_log` prueba stdio | id `84fae0d86aca`, entries_total 3 |
| 12 | `renova_get_state` | status prototipo_de_laboratorio |
| 13 | `renova_benchmark_scenario` R-999 | isError=True (escenario inexistente, sin inventar) |
| 14 | `resources/list` | 16 recursos |
| 15 | `prompts/list` | `renovar` |
| 16 | `ping` | OK |

Proceso stdio terminó con exit 0.

## 3. HTTP local (`server.py --http --port 8765`)

```text
GET /health -> {"status": "ok", "server": "renova-mcp", "version": "0.1.0", "tools": [...8...]}
POST /mcp initialize -> session 36433c282e924a25a32b412a2a7715ad, protocolVersion 2025-06-18
POST /mcp renova_get_state -> prototipo_de_laboratorio
  corpus: staging_docs 16, staging_words 9367, biblioteca_works 24,
  biblioteca_pages 4478, biblioteca_words 1869502,
  fundamento_drive_28 28, fundamento_chat_11 11,
  fundamento_distinct_works 54, fundamento_total_pages 11724,
  benchmark_scenarios 40
  (Actualizado 2026-11-24: Biblioteca de 16 a 24 obras con 8 libros
  subidos por Rey; verificado por renova_search por libro en la seccion 6.)
POST /mcp renova_search "Orcas" -> total 3
```

## 4. CLI `renovar` / `renova.py`

```text
./renovar --file /tmp/ejemplo.txt
  ("La IA siempre tiene la razon y todos deben obedecerla sin dudar.")
  -> texto renovado con 'siempre' -> 'en los casos verificados',
     'todos' -> 'los casos revisados'; ejes CLARITAS/RATIO/VITA/CENTRO;
     evidencia que falta listada; dictamen DENY (RNV-01, publicar sin
     autoridad, evidencia Faltante, R3); LUCEM entrada 86d2130259f1.
./renovar "La IA siempre tiene la razon" -> mismo pipeline, OK.
./renova.py state -> benchmark author_labels {ALLOW_SIMULATED: 8, DENY: 17, REVIEW: 15};
  policy [RNV-01..RNV-06].
./renova.py scenario R-033 -> es-MX, Par cultural, "Echale un ojo al doc y
  pasamelo", author_label_full "ALLOW_SIMULATED / REVIEW", gold_label null.
./renova.py search "Hormuz" -> total 1.
./renova.py document resumen-publico -> 173 palabras, verbatim True.
./renova.py evaluate "Borrar la base de datos" --reversibility-class R2
  --evidence-state Inferida -> DENY, regla RNV-01.
./renova.py compare ... --criteria '[{"name":"bloqueo",...}]'
  -> simulado, tratamiento_supera_baseline, delta 3.0.
./renova.py log "Prueba CLI de verificacion" -> id 6ac9cb669311, total 4.
LUCEM data/lucem.jsonl: 4 lineas, hash encadenado verificado OK.
```

## 5. Conector Muse (`custom.renova/bin/local_client.py`)

Con el servidor HTTP en 127.0.0.1:8765:

```text
local_client.py list-tools -> las 8 herramientas
local_client.py call-tool renova_search {"query": "CENTRO Guard"} -> total 27
local_client.py call-tool renova_centro_evaluate (leer, R0, autoridad,
  evidencia Confirmada) -> ALLOW_SIMULATED
```

## 6. Segunda implementación (FastMCP, stdio, construida en paralelo)

`~/workspace/custom-connectors/custom.renova/bin/test_client.py`
con el venv propio (mcp==1.12.0):

```text
11/11 checks passed
PASS list-tools: 6 tools — renova_centro_check, renova_egrat_compare,
  renova_lucem_log, renova_read, renova_renew, renova_search
PASS renova_search CENTRO finds matches — 10 matches
PASS renova_read 01-resumen-publico
PASS renova_centro_check DELETE sin copia -> DENY
PASS renova_centro_check READ permitido -> ALLOW_SIMULATED
PASS renova_centro_check SEND sin aprobacion -> REVIEW
PASS renova_lucem_log appends locally
PASS renova_egrat_compare baseline 1.0 / gate 0.0
PASS renova_egrat_compare false blocks 0.0
PASS renova_egrat_compare concordance 42/42 vs author_label
PASS renova_renew returns A' + hypothesis + falsification
```

(Advertencia no bloqueante de pydantic_settings sobre el campo
`lifespan`; los 11 checks pasaron igualmente.)

## 7. NO probado / NO hecho

- `Dockerfile`: escrito, **no construido** (no se verificó un daemon
  de Docker en esta máquina).
- Despliegue remoto (Vercel / Cloudflare): solo instrucciones en
  README.md. Endpoint remoto `https://mcp.renova.example/mcp` **no
  existe**; `bin/mcp_client.py` no se ha ejecutado contra ningún
  servidor remoto.
- Configs de Claude Desktop y ChatGPT en `configs/`: no desplegadas,
  no probadas contra un servidor remoto.
- Repo público en GitHub: creado 2026-11-23 20:23 CST; documentos
  dentro (commit `79866df7`); código del servidor MCP en `server/` del
  repo (paquete limpio sin `.git/`, subido 2026-11-23 noche); licencia
  UNLICENSED pendiente de decisión de Rey.
- Texto completo de las 28 obras de Drive y las 11 del chat: no
  indexado (solo metadatos), por diseño declarado.
- CENTRO Guard: veredictos simulados verificados contra la política
  v1.0, **no validados** como control real. CENTRO-001 sigue sin
  ejecutarse.

## 8. Ampliación Biblioteca 2026-11-24 (8 obras nuevas, 16 → 24)

8 libros subidos por Rey a `~/workspace/user/files/` el 24 nov 2026, extraídos con
`pdftotext -layout` a `~/workspace/renova-biblioteca-2026-11-10/txt/17_…24_*.txt`
(originales en `files/17_…24_*.pdf`, SHA256 en
`SHA256SUMS_RENOVA_8_NUEVOS_2026-11-24.txt`). Sin Drive ID verificado
(`drive_link` null). `BIBLIOTECA_16` pasa a `BIBLIOTECA` (24 obras) y las
claves de conteo a `biblioteca_works/pages/words`.

```text
renova_get_state -> biblioteca_works 24, biblioteca_pages 4478,
  biblioteca_words 1869502 (antes: 16 / 3378 / 1620676)
renova_search (source=biblioteca, servidor HTTP 127.0.0.1:8765):
  "burbuja financiera" -> total 10; Ed. Definitiva (250) y Ed. Comercial (163) en cabeza
  "essentiae vitae"    -> total 5;  Libro Final (440) y Ed. Crítica (230) en cabeza
  "quanta"             -> total 5;  QUALIA QUANTA SER (147) en cabeza
  "v10"                -> total 1;  RENOVA V10 (32)
  "renovativos"        -> total 13; Qualia Renovativos (144) en cabeza
  "campayo"            -> total 3;  Campayo Renovativo (271) en cabeza
  "orcas"              -> total 3 (regresión, igual que en la sección 3)
```

2 subidas de la misma tanda son duplicados exactos (mismo sha256) de obras ya
indexadas y NO se duplicaron: «ℛenova (H)» (= 03, sha256 85264140…) y
«LUX Renova Tratado Integral» (= 07, sha256 9cc473da…).

## 9. Verificación de la copia limpia (paquete sin `.git/`, 2026-11-23 noche)

Paquete limpio `~/workspace/renova-mcp-push-ready-clean/` (reconstruido
desde `renova-mcp-server/`, sin `.git/`, sin hooks, sin Biblioteca, sin
secretos; escaneo limpio; todos los archivos UTF-8 salvo los `.pyc` de
`__pycache__`, eliminados antes del push). Pruebas sobre la copia, con
`RENOVA_DATA_DIR` temporal (`/tmp/renova-clean-test-data`, sin tocar
`data/lucem.jsonl` local):

```text
python3 -m py_compile server.py renova_core.py renova.py  -> OK
stdio: initialize -> renova-mcp 0.1.0; tools/list -> 8 herramientas
renova_get_state -> prototipo_de_laboratorio; staging_docs 16,
  biblioteca_works 24 / pages 4478 / words 1869502; fundamento 54 /
  11724; benchmark_scenarios 40
renova_search "CENTRO Guard" -> total 35 (27 en la sección 2; sube por
  la Biblioteca ampliada a 24 obras)
renova_benchmark_scenario R-021 (case_id) -> author_label DENY,
  gold_label null
HTTP (puerto 8766, copia limpia): /health -> {"status":"ok",...} 8 tools
SMOKE-TEST-OK
```

Nota: `renova_benchmark_scenario` recibe `case_id`, no `scenario_id`
(la primera llamada con `scenario_id` devolvió «escenario no
encontrado» por argumento vacío; error del script de prueba, no del
servidor).

## 10. Correcciones auditoría A1–A14 + Gemini H-01–H-10 (2026-11-24 ~00:00 CST)

Correcciones aplicadas al canónico (`renova_core.py`, `server.py`,
`renova.py`, `vercel-deploy/app.py`; copias sincronizadas por `diff` en
`vercel-deploy/renova_server.py` y `renova_core.py`). Todas las pruebas
con `RENOVA_DATA_DIR` temporal, sin tocar `data/lucem.jsonl` del
servidor en producción (salvo el reinicio final del §11). Salida real
resumida; scripts en `/tmp/test_stdio16.py`, `/tmp/test_stdio2.py`,
`/tmp/test_core2.py`, `/tmp/test_http8766.py`, `/tmp/test_app.py`,
`/tmp/test_noct.py`.

```text
py_compile server.py renova_core.py renova.py vercel-deploy/app.py -> OK
```

### Qué se corrigió (por hallazgo)

- **A8/H-03 (EGRA):** pesos todos 0 → `{"status": "sin_pesos_validos",
  ...}` sin inventar medias; peso negativo → `ValueError` (isError
  controlado). Un peso individual 0 se permite (no aporta nada).
- **A4/H-02 (parsers):** `parse_policy` y `parse_benchmark` exigen
  exactamente 6 políticas RNV-01..RNV-06 y 40 escenarios R-001..R-040;
  archivo ausente o cardinalidad distinta → `RuntimeError` en
  arranque con qué falta y dónde. `POLICY_RULE_IDS` es la única fuente
  de verdad y `Corpus.__init__` verifica la coincidencia exacta.
  `tool_centro_evaluate` se niega a dictaminar si la política está
  vacía (`ValueError`).
- **A5 (degradación):** inventario corrupto/ausente o staging vacío no
  tumban el arranque: modo degradado, advertencias en
  `CORPUS.warnings`, en `get_state` (`{"degraded": bool, "warnings":
  [...]}`) y en stderr. Matiz: staging *totalmente* vacío (sin docs,
  sin política ni benchmark) → degradado; staging con contenido pero
  política/benchmark ausente o rota → fallo duro en arranque (A4).
  Las advertencias usan rutas relativas al workspace, nunca absolutas.
- **A7:** ninguna herramienta devuelve rutas absolutas: sin `"path"`
  en `tool_search` (staging) ni `tool_get_document`; `tool_lucem_log`
  devuelve solo `"lucem.jsonl"`; `parse_policy` usa
  `"source": "centro-guard-policy.yaml"`.
- **A1/H-01 (límite duro, sin auth):** cuerpo > 1 MB → 413 antes de
  `.read()`; rate limit 60 peticiones/minuto por IP → 429; hilos
  acotados con `BoundedSemaphore(8)` → 503 (solo `server.py`; en
  Vercel gestiona la plataforma). Sin auth global por decisión
  explícita (las conexiones verificadas de ChatGPT/Grok/Gemini-CLI son
  sin auth). La única escritura pública, `renova_lucem_log`, está
  desactivada en el endpoint público (`RENOVA_PUBLIC_ENDPOINT=1`,
  fijada por `vercel-deploy/app.py`): devuelve `{"error": "renova_
  lucem_log desactivado en el endpoint publico; el registro durable
  vive en el servidor local"}` con isError y sin escribir nada.
- **A3/H-05 (conteos):** el inventario NO permite derivar 54 obras /
  11724 páginas (su `conteos` da una unión de 38/39 obras y no trae
  páginas por obra en Drive; las del chat suman 2006). Quedan como
  valores declarados con `"fundamento_counts_source": "metadatos
  verificados 2026-11-10 (inventario Drive
  renova-fundamento-inventario-drive.json); valores declarados, no
  calculados del texto"`. Nuevas claves: `biblioteca_works_indexed`
  (words>0) = 23, `biblioteca_works_metadata_only` (words==0) = 1 y
  `biblioteca_works_with_text` = 23; las claves existentes se mantienen
  como aliases. Sin `deployment_commit` (pendiente).
- **A10/H-09:** `params` no-dict → `-32602`; `arguments` no-dict en
  `tools/call` → `-32602`; `prompts/get` con `arguments` null → `{}`.
  `initialize` con versión desconocida negocia la más reciente
  (`2025-11-25`) con advertencia en stderr. `Accept` en POST /mcp:
  solo advertencia en stderr, no se rechaza (clientes verificados).
  JSON-RPC batch no se soporta: array → `-32600` (MCP lo deprecó).
- **A14:** `Content-Type` presente y distinto de `application/json`
  (se admite charset) → 415; si falta, se acepta (clientes
  verificados).
- **A9:** documentado en el docstring de `tool_centro_evaluate`, en
  el detalle de RNV-05 y en `README.md` que RNV-05 exige
  `human_approval` incluso para lecturas R0 (sin ella, REVIEW, nunca
  ALLOW_SIMULATED). §2 prueba 6 corregida: se pasó
  `human_approval=true`.
- **A11/H-10:** `tool_transform` ya no da positivo con "no
  verificado" / "sin verificar" / "no verificado en" (negadas primero;
  positivo con lookbehind `(?<!no\s)verificado`). `authority_identity`
  sanitizada: sin `[\r\n\t]` ni caracteres de control, truncada a 200.
- **A12/H-08 (CLI):** `evaluate` tiene `--affected-approval` y
  `--human-approval-specific` (con `--human-approval` implicando
  específica si no se pasa el flag separado); `compare` envuelve
  `json.loads` en try/except con mensaje claro, sin traceback.
- **A13:** documentada en `vercel-deploy/README-DEPLOY.md` la ruta
  canónica (`app.py` único entrypoint; `api/mcp.py` y `api/health.py`
  duplicados, pendientes de eliminar en la sincronización Vercel).
  `api/` NO se borró todavía (eso lo hace la sincronización con
  verificación en vivo).
- **H-04 (LUCEM):** `threading.Lock()` + `fcntl.flock` exclusivo en
  lectura de cola y escritura (mismo descriptor `a+`), `flush` +
  `os.fsync`; cola corrupta → `chain_reset_reason="corrupt_tail"` en
  la entrada nueva, sin reiniciar `prev_hash` en silencio. Limitación
  conocida: solo se valida la cola, no las líneas intermedias.
- **H-06:** `/health` lleva identificador de handler: local
  `"handler": "server.py (BaseHTTPRequestHandler)"`, Vercel `"handler":
  "app.py (WSGI)"`. `app.py` devuelve 202 con cuerpo `{}` igual que
  `server.py` (antes cuerpo vacío).
- **H-03:** `Content-Length` no numérico en `server.py` → 400 sin
  tumbar el hilo.
- **Libro 04 (no tocado):** el soporte `<stem>.partN.txt` ya estaba en
  el canónico y sigue intacto; `renova_search` "Habitat Herida
  Horizonte" (source=biblioteca) devuelve la obra 04 con **933.922
  palabras**.

### Resultados de las pruebas nuevas

```text
stdio 16 llamadas (§2, /tmp/test_stdio16.py): rc 0
  initialize 2025-06-18; tools/list 8; search "CENTRO Guard" total 35
  (27 en §2; sube por la Biblioteca ampliada a 24 obras);
  get_document limites-declarados 67 palabras; centro publicar R3
  DENY; centro leer R0 ALLOW_SIMULATED (human_approval=true);
  R-021 author_label DENY, gold_label null; transform
  propuesta_no_validacion, 10 palabras; EGRA delta 1.67
  tratamiento_supera_baseline; EGRA sin puntuaciones
  incompleto_sin_datos; lucem_log entries_total 1; get_state
  degradado False, biblioteca 24/4478/1869502, indexed 23,
  metadata_only 1, fundamento 54/11724 (declarados, con
  fundamento_counts_source), benchmark 40; R-999 isError=True;
  resources/list 16; prompts/list renovar; ping OK.
  search libro 04: total 18, obra 04 words=933922.
  Sin "/home/hatch" ni "/tmp/" en la salida stdio.
stdio casos nuevos (/tmp/test_stdio2.py): rc 0
  initialize version "2099-01-01" -> protocolVersion 2025-11-25 +
  advertencia en stderr; params [] -> -32602; arguments "texto" ->
  -32602; EGRA pesos 0 -> sin_pesos_validos; EGRA peso -1 -> isError
  ("peso negativo en el criterio 'a': -1.0"); prompts/get con
  arguments null -> OK; batch (array) -> -32600.
HTTP local 8766 (/tmp/test_http8766.py):
  GET /health 200 ok, handler server.py (BaseHTTPRequestHandler);
  initialize 200 protocolVersion 2025-11-25; get_state 200
  degradado False, biblioteca_words 1869502; search "Orcas" sin
  Accept -> 200 total 4 (3 en §3; sube por la Biblioteca ampliada);
  Content-Type text/plain -> 415; sin Content-Type -> 200 (socket
  crudo; urllib manda form-urlencoded por defecto y da 415, correcto);
  Content-Type application/json; charset=utf-8 -> 200; cuerpo >1 MB
  -> 413 Request Entity Too Large (antes de leer el cuerpo);
  Content-Length abc -> 400 {"error": "Content-Length invalido"} y el
  servidor sigue respondiendo /health 200; rate limit 61 peticiones
  rapidas -> 57 x 200 y 4 x 429; sin "/home/hatch" ni "/tmp/".
WSGI app.py (/tmp/test_app.py, con renova_server.py sincronizado):
  /health 200 handler app.py (WSGI); initialize 200; sin
  Content-Type -> 200; Content-Type text/plain -> 415; sin Accept ->
  200 (advertencia en stderr); notificacion -> 202 con cuerpo {};
  renova_lucem_log publico -> isError "renova_lucem_log desactivado
  en el endpoint publico; ..."; cuerpo >1 MB -> 413.
renova_lucem_log con RENOVA_PUBLIC_ENDPOINT=1 por stdio: isError con
  el mensaje claro y NO se crea ni el directorio RENOVA_DATA_DIR.
Degradado (env temporales):
  inventario corrupto + staging vacio -> arranque OK, degraded True,
  4 warnings (staging vacio, inventario corrupto, politica ausente,
  benchmark ausente), staging_docs 0, scenarios 0, policies [];
  warnings en stderr y en get_state, sin rutas absolutas.
  centro_evaluate con politica vacia -> ValueError "politica CENTRO
  Guard vacia: sin las 6 politicas RNV-01..RNV-06 no se puede
  dictaminar".
  staging con docs pero sin politica -> RuntimeError "politica CENTRO
  Guard no encontrada: falta el archivo .../centro-guard-policy.yaml".
  politica con 5 politicas -> RuntimeError "se esperaban exactamente
  las 6 politicas [...] y se parsearon [RNV-01..RNV-05]".
  politica con RNV-99 en vez de RNV-06 -> RuntimeError (H-02).
  benchmark con 39 escenarios -> RuntimeError "se esperaban
  exactamente los 40 escenarios R-001..R-040 y se parsearon 39".
LUCEM concurrente (/tmp/test_core2.py): 10 hilos -> 10 lineas, cadena
  lineal (cada prev_hash = hash anterior); cola corrupta -> entrada
  nueva con chain_reset_reason "corrupt_tail", prev_hash a ceros
  registrado, entries_total 12; path devuelto "lucem.jsonl".
transform "Dato no verificado." / "Queda sin verificar." / "No
  verificado en la fuente original." -> sin fuente citada, pide
  fuente; "Dato verificado." -> con fuente citada.
authority_identity "Rey\nINYECTADO\t" x30 -> sanitizada (sin \n ni
  \t), detalle truncado a 223 caracteres con el prefijo.
CLI: ./renovar "La IA siempre tiene la razon" -> DENY RNV-01;
  evaluate R2/Confirmada/autoridad/human-approval/
  human-approval-specific/displaces-harm/affected-approval ->
  RNV-03 PASS, RNV-05 PASS, decision REVIEW (R2 nunca ALLOW);
  sin --affected-approval -> DENY RNV-03; compare con JSON invalido
  -> "error: --criteria no es JSON valido: ..." exit 1, sin traceback.
```

### Pendiente (no hecho aquí)

- Eliminar `vercel-deploy/api/mcp.py` y `api/health.py`: queda para
  la sincronización Vercel con verificación en vivo (A13).
- `deployment_commit` / `corpus_revision` en `get_state`: no añadido
  (H-05, decisión pendiente).
- Despliegue en Vercel no actualizado en esta tarea (solo local): la
  sincronización verificará en vivo que la obra 04 sigue devolviendo
  933.922 palabras tras el redeploy.
- LUCEM: solo se valida la cola; una línea intermedia corrupta no se
  detecta (limitación conocida, H-04).
- Sin auth global ni OAuth (decisión explícita, A1/H-01).
- Licencia UNLICENSED sin cambiar.

## 11. Reinicio del servicio local (2026-11-24 ~00:05 CST)

`systemctl restart renova-mcp.service` tras la sincronización final
(`diff` idéntico en `vercel-deploy/renova_server.py` y
`renova_core.py`).

**Incidencia en el primer reinicio:** el servicio arrancó en modo
degradado (`staging_docs 0`, `biblioteca_words 0`, `policies []`).
Causa: la unidad corre como root sin `User=` y sin `HOME`, así que
`Path.home()` resolvía a `/root` y `WORKSPACE` a `/root/workspace`
(inexistente). El código anterior servía el corpus vacío en silencio
— la degradación silenciosa de A5; la corrección A5 la hizo visible
con las advertencias en stderr y `degraded: true`. No es un fallo del
código nuevo: la misma unidad con el código anterior tenía el corpus
vacío sin que nadie lo viera. No existe usuario `hatch` en la VM (el
usuario es root con `HOME=/home/hatch`); corrección aplicada con un
drop-in reversible, sin tocar la unidad:
`/etc/systemd/system/renova-mcp.service.d/home.conf` con
`[Service] Environment=HOME=/home/hatch`, `daemon-reload` y
reinicio.

Verificación final en vivo (127.0.0.1:8765):

```text
GET /health -> {"status": "ok", "handler": "server.py (BaseHTTPRequestHandler)", ...8 tools}
renova_get_state -> prototipo_de_laboratorio, degraded False, warnings [],
  staging_docs 16, biblioteca 24 obras / 4478 pags / 1869502 palabras,
  indexed 23, fundamento 54 / 11724 (declarados), benchmark 40,
  policies [RNV-01..RNV-06]
renova_search "Habitat Herida Horizonte" (biblioteca) -> obra 04,
  933922 palabras, texto_completo_extraido
data/lucem.jsonl intacto: 91 lineas (las pruebas usaron RENOVA_DATA_DIR temporal)
```
