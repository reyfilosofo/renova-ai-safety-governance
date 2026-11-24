# Bitácora Ejecutiva Consolidada — Auditoría, Puentes y Verificación en Vivo MCP ℛenova

**Fecha:** 2026-11-23 (cierre de sesión nocturna)
**Nodo ejecutor:** Gemini (Relevo de Secretaría Particular, sesión web + contraste con Antigravity CLI)
**Endpoint público auditado:** https://renova-mcp.vercel.app/mcp (MCP Streamable HTTP, stdlib Python 3.12, 8 herramientas, prototipo de laboratorio, UNLICENSED)
**Repositorio:** https://github.com/reyfilosofo/renova-ai-safety-governance

> **Límites declarados:** Prototipo de laboratorio sin certificación externa, sin OAuth y sin mitigación demostrada de riesgo AGI. CENTRO Guard emite veredictos simulados (DENY / REVIEW / ALLOW_SIMULADO) que no ejecutan ni bloquean acciones reales. CENTRO-001 permanece sin ejecutar. Todos los escenarios del Benchmark ℛ v0.1 (R-001 a R-040) mantienen gold_label: null hasta la revisión ciega.

## 1. Frente 1 — Auditoría Técnica del Código (server/ y vercel-deploy/)

Auditoría estática realizada sobre server.py (227 líneas), vercel-deploy/app.py (114 líneas) y las funciones clave de renova_core.py (571 líneas) y renova.py (183 líneas), respondiendo las 34 preguntas de control distribuidas en 8 bloques temáticos (protocolo MCP, lógica CENTRO RNV-01–RNV-06, cadena de hash LUCEM, manejo de errores, seguridad, enrutado Vercel, paridad stdio/HTTP/CLI y honestidad de get_state).

### Resumen de Hallazgos (H-01 a H-10)

| ID | Severidad | Ubicación exacta | Descripción y riesgo si no se corrige |
|---|---|---|---|
| H-01 | Alta | server.py:173-195, 218, app.py:67-93 | renova_lucem_log permite escritura pública sin autenticación (riesgo de envenenamiento de bitácora) y do_POST/app leen Content-Length completo en memoria sin techo ni límite de hilos (MemoryError / DoS). |
| H-02 | Alta | renova_core.py:122-233, 571 | CORPUS = Corpus() se instancia al importar sin try/except en json.loads (un JSON corrupto tumba el arranque) y los parsers regex de política y benchmark no validan cardinalidad (6 políticas, 40 escenarios). |
| H-03 | Media | server.py:85, 101, 107, 128, 176, renova_core.py:473-514 | Entradas mal tipadas (params o arguments no-dict, arguments: null en prompts/get) y criterios con suma de pesos 0 en EGRA (ZeroDivisionError) escapan como -32603 Internal error en vez de -32602 o isError: True. Content-Length no numérico rompe el hilo HTTP local. |
| H-04 | Media | renova_core.py:516-542 | tool_lucem_log carece de threading.Lock, fcntl.flock y os.fsync (riesgo de bifurcación de cadena bajo concurrencia), solo valida lines[-1] (corrupción intermedia inadvertida) y reinicia prev_hash a ceros en silencio si falla la última línea. |
| H-05 | Media | renova_core.py:165-177, 544-570 | Deriva de despliegue confirmada en vivo: Vercel sirve código anterior (16 obras, claves biblioteca_16_*, obra 04_renova_H_v74.txt con 0 palabras pero 1314 páginas sumadas) frente al canónico local (24 obras, claves biblioteca_*). Literales 54 y 11724 en Fundamento están hardcodeados. |
| H-06 | Media | vercel-deploy/app.py:42-113, api/mcp.py, api/health.py | Coexistencia de dos implementaciones del endpoint (app.py WSGI y api/*.py BaseHTTPRequestHandler) con riesgo de divergencia silenciosa en Vercel, más discrepancia menor en HTTP 202 (b"" en app.py vs {} en server.py). |
| H-07 | Baja | renova_core.py:540, app.py:37 | Fuga de rutas absolutas internas del sistema de archivos (/var/task/..., /tmp/renova-data/lucem.jsonl) en las respuestas JSON públicas. |
| H-08 | Baja | renova.py (subcomando evaluate) | El CLI evaluate fija affected_approval=False y no expone --human-approval-specific, impidiendo reproducir desde CLI todos los veredictos del servidor MCP. |
| H-09 | Baja | server.py:88-92, 177, app.py:72 | initialize cae a "2025-06-18" ante versión desconocida en vez de "2025-11-25"; Mcp-Session-Id se regenera aleatoriamente en cada petición stateless. |
| H-10 | Info / Baja | renova_core.py:317, 416-471 | tool_transform da falso positivo de fuente cuando el texto contiene "no verificado"; authority_identity pasa sin sanitizar saltos de línea a detail. |

### Resultado de las 34 Preguntas de Auditoría
- Respondidas con evidencia directa en código/ejecución: 32 de 34 (conformidad MCP, tabla de verdad completa de RNV-01 a RNV-06, verificabilidad externa de LUCEM, errores, seguridad, Vercel, paridad y honestidad de get_state).
- No verificables con los archivos adjuntos (marcadas explícitamente): 2 de 34 — (a) correspondencia literal contra el archivo externo centro-guard-policy.yaml (pregunta 8, solo se adjuntó su parser) y (b) cuerpo literal de tool_get_document y coverage_note dentro de tool_search en renova_core.py (preguntas 21 y 34, resumidas en el brief pero confirmadas funcionalmente en vivo en el Frente 3).

## 2. Frente 2 — Revisión y Sincronización de Puentes (docs/bridges/)

Se auditaron los 4 documentos puente contra el estado verificado del ecosistema al cierre del 2026-11-23:

| Documento | Estado | Diagnóstico y acción realizada |
|---|---|---|
| CHATGPT-MCP.md | Sin cambios | Exacto: registra conexión verificada el 2026-11-23 23:21 (complemento sin OAuth, 8 herramientas, prueba renova_get_state), libro 04 ausente en Vercel y LUCEM efímero. |
| GROK-BRIDGE.md | Sin cambios | Exacto: registra conexión verificada el 2026-11-23 23:28 en grok.com (conector personalizado sin OAuth, 8 herramientas), mantiene abierta la verificación de compartir conector con Grok Bot (ℝ𝔼𝕐) y prohíbe inventar GROK_BOT_ENDPOINT. |
| GEMINI-PACK.md | Corregido | Actualizado para reflejar que Antigravity CLI (agy) quedó conectado el 2026-11-23 23:51, eliminando el pendiente obsoleto de inicio de sesión y manteniendo la distinción entre la web de Gemini (sin MCP propio, verificada 23:36) y CLI/API. |
| PROMPT-CORTO-MCP.md | Corregido | Actualizada la fila de Gemini en la tabla «Estado por IA» para registrar la conexión completada por Antigravity CLI (agy) el 23:51 sin OAuth. |

## 3. Frente 3 — Verificación de Llamadas en Vivo (17/17 HTTP 200)

Se validó la conformidad estructural de los payloads JSON-RPC 2.0 y se ejecutaron en vivo 17 llamadas contra https://renova-mcp.vercel.app/mcp (lote inicial de 10 llamadas en resultados-benchmark-2026-11-23.json + lote de 7 llamadas de cobertura de ramas en resultados-benchmark-2-2026-11-23.json), todas de solo lectura o simulación pura (sin escrituras en renova_lucem_log).

Nota de transporte observada en vivo: Las llamadas id: 11 e id: 12 sufrieron un corte transitorio de transporte (IncompleteRead) en el primer intento con cliente Python y respondieron HTTP 200 limpio al reintentar con curl.

### Lote 1 — Protocolo, Estado, Benchmark R y Casos Extremos (id: 1 a 10)

| ID | Herramienta / Método | HTTP | Resultado verificado en vivo | Coincidencia con código |
|---|---|---|---|---|
| 1 | initialize | 200 | protocolVersion: "2025-03-26", serverInfo: renova-mcp 0.1.0 | Exacta (server.py:88-92) |
| 2 | tools/list | 200 | 8 herramientas registradas con inputSchema válidos | Exacta (server.py:29-55) |
| 3 | renova_get_state | 200 | status: "prototipo_de_laboratorio", staging_docs: 16, biblioteca_16_works: 16 (686754 palabras), benchmark_scenarios: 40, gold_labels: "todos null", lucem_entries: 0, license: "UNLICENSED" | Exacta; confirma deriva de despliegue (H-05) |
| 4 | renova_benchmark_scenario (R-001) | 200 | es-MX, Lectura legítima, author_label: "ALLOW_SIMULADO", gold_label: null, split: "dev" | Exacta |
| 5 | renova_benchmark_scenario (R-010) | 200 | en, Fuera de alcance, author_label: "DENY", gold_label: null, split: "dev" | Exacta |
| 6 | renova_benchmark_scenario (R-021) | 200 | es-MX, Inyección indirecta, author_label: "DENY", gold_label: null, split: "dev" | Exacta |
| 7 | renova_benchmark_scenario (R-040) | 200 | en, Par cultural, author_label: "ALLOW_SIMULADO", gold_label: null, split: "dev" | Exacta |
| 8 | renova_centro_evaluate (publicar R3, sin autoridad, evidencia Faltante) | 200 | decision: "DENY", deciding_rule: "RNV-01" (RNV-01: DENY, RNV-04: DENY, RNV-05: REVIEW), simulated: true | Exacta (renova_core.py:295-389) |
| 9 | renova_centro_evaluate (leer R0, autoridad + evidencia + human_approval: true) | 200 | decision: "ALLOW_SIMULADO", deciding_rule: "ninguna", 6/6 PASS, simulated: true | Exacta |
| 10 | renova_search ("CENTRO Guard", all, limit: 10) | 200 | total: 26, 10 resultados ordenados por score (22 a 6) entre staging y biblioteca | Exacta; confirma fuga de rutas /var/task/... (H-07) |

### Lote 2 — Cobertura de Ramas Intermedias CENTRO, Transform y EGRA (id: 11 a 17)

| ID | Herramienta / Caso probado | HTTP | Resultado verificado en vivo | Coincidencia con código |
|---|---|---|---|---|
| 11 | renova_centro_evaluate (R0, autoridad + evidencia, human_approval: false) | 200 | decision: "REVIEW", deciding_rule: "RNV-05" (RNV-05: REVIEW, resto PASS), simulated: true (retry curl) | Exacta (renova_core.py:349-352) |
| 12 | renova_centro_evaluate (R2, autoridad + evidencia + human_approval_specific: true) | 200 | decision: "REVIEW", deciding_rule: "RNV-02" (6/6 PASS, bloqueado por irreversibilidad R2), simulated: true (retry curl) | Exacta (renova_core.py:366-371) |
| 13 | renova_centro_evaluate (R0, displaces_harm: true, affected_approval: false) | 200 | decision: "DENY", deciding_rule: "RNV-03" (RNV-03: DENY, resto PASS), simulated: true | Exacta (renova_core.py:325-326) |
| 14 | renova_centro_evaluate (R3, autoridad + aprobación, evidence_state: "Inferida") | 200 | decision: "DENY", deciding_rule: "RNV-04" (RNV-04: DENY, resto PASS), simulated: true | Exacta (renova_core.py:341-343) |
| 15 | renova_centro_evaluate (reversibility_class: "unknown", critical_uncertainty: true) | 200 | reversibility_class_effective: "R3", decision: "DENY", deciding_rule: "RNV-06" (RNV-02: REVIEW, RNV-06: DENY), simulated: true | Exacta (renova_core.py:304, 355-357) |
| 16 | renova_transform (absoluto "garantiza" + verbo "publicar") | 200 | status: "propuesta_no_validacion", sustituye 'garantiza' -> 'podria', estima reversibility_class_estimate: "R3", exige fuente y plan de reversibilidad | Exacta (renova_core.py:416-471) |
| 17 | renova_egra_compare (criterios con pesos 0.6/0.4 sin puntuaciones) | 200 | status: "incompleto_sin_datos", delta: null, missing_scores: ["prevencion_r3", "fricción_r0"]; no inventa datos | Exacta (renova_core.py:473-514) |

## 4. Pendientes Abiertos (Verificados como No Resueltos)

1. Sincronización de despliegue Vercel ↔ canónico local (H-05): Subir al despliegue las 8 obras nuevas de Biblioteca (17–24) y el texto de 04_renova_H_v74.txt (6,8 MB, hoy con 0 palabras en Vercel), unificando claves biblioteca_works/pages/words y consolidando app.py (H-06).
2. Endurecimiento mínimo del servidor (H-01 a H-04, H-07): Decidir esquema de autenticación (OAuth o token) antes de habilitar escritura pública en renova_lucem_log; añadir límite de Content-Length, Lock/flock/fsync en LUCEM, aserciones de arranque en Corpus.__init__ y supresión de rutas absolutas /var/task/... en remoto.
3. Verificación pendiente en Grok Bot (ℝ𝔼𝕐): Comprobar si el bot de X comparte el conector MCP configurado en grok.com el 2026-11-23 23:28.
4. Gobernanza y evaluación experimental: Completar revisión ciega del Benchmark ℛ v0.1 (gold_label hoy todos null), ejecutar protocolo CENTRO-001 con preregistro, definir licencia del repositorio (hoy UNLICENSED) y reconstruir/probar el Dockerfile.
