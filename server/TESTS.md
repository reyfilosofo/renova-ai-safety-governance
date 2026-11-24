# Pruebas del servidor MCP ℛenova — resultados reales

Fecha: 2026-11-23. Servidor: `renova-mcp-server/` v0.1.0 (stdlib, sin
dependencias). Nada de lo aquí anotado es una prueba en público ni una
validación externa: son llamadas locales contra los archivos canónicos.

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
| 6 | `renova_centro_evaluate` leer, R0, autoridad verificada, evidencia Confirmada | **ALLOW_SIMULATED** |
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
