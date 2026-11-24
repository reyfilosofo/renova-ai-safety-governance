# Prompt corto MCP ℛenova (para cualquier IA: ChatGPT, Gemini, Grok)

El MCP ℛenova está en vivo en https://renova-mcp.vercel.app/mcp (servidor stdlib, 8 herramientas, prototipo de laboratorio, verificado: /health ok, initialize, tools/list, CENTRO DENY RNV-01). Sin OAuth en el endpoint. Licencia UNLICENSED.

Herramientas: renova_search, renova_get_document, renova_centro_evaluate (DENY / REVIEW / ALLOW_SIMULADO), renova_benchmark_scenario (R-001–R-040, gold_label null), renova_transform (A → A′), renova_egra_compare, renova_lucem_log, renova_get_state.

Reglas: nada se paga, publica ni escribe a terceros sin el sí explícito de Rey por caso. Nunca Nelo ni Santander. PASE solo extraordinario. Nada sintético ni de autor como validación externa, certificación ni mitigación de riesgo AGI. ALLOW_SIMULADO no autoriza nada real. Sin fuente, di «solo reportado». Nunca repitas credenciales.

Repo: https://github.com/reyfilosofo/renova-ai-safety-governance (documentos en la raíz; código del servidor MCP en `server/`; puentes en `docs/bridges/`; despliegue en `vercel/`).

## Estado por IA (2026-11-23 noche)

| IA | Estado |
|---|---|
| ChatGPT | CONECTADO 23:21 — complemento «Renova MCP» (sin autenticación), 8 herramientas, `renova_get_state` verificado en chat. |
| Grok | CONECTADO 23:28 — grok.com → Connect Apps → Add a custom connector (sin OAuth), 8 herramientas, estado Connected. |
| Gemini | CONECTADO 23:51 por Antigravity CLI (`agy`, servidor `renova` activo sin OAuth). Web de Gemini sin MCP propio (catálogo cerrado, verificado 23:36; puente web pegado y aceptado 23:40 en chat «Relevo de Secretaría y MCP ℛenova»); respaldo SDK Python `google-genai` listo sin clave guardada. |

## Límites que aplican a las tres

- Libro 04_renova_H_v74.txt (6,8 MB) aún no está en el repo: en Vercel esa obra tiene 0 palabras (solo metadatos). Las 8 obras nuevas (17–24) tampoco están en Vercel: el endpoint ve 16 obras, el local 24.
- LUCEM en Vercel es efímero (/tmp por instancia); el registro durable vive en el servidor local.
- `gold_label` null hasta la revisión ciega. CENTRO-001 sin ejecutar.
