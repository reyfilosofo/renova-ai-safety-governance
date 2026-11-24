# ChatGPT — conectar el MCP ℛenova

## Estado: CONECTADO 2026-11-23 23:21 (verificado en vivo)

Endpoint público en vivo desde 2026-11-23 23:11: https://renova-mcp.vercel.app/mcp
(verificado: initialize + tools/list con 8 herramientas + CENTRO DENY RNV-01).
Sin OAuth en el endpoint.

Conexión verificada: complemento «Renova MCP» en Configuración →
Integraciones → Complementos → «Explorar catálogo» → «Agregar» → «Agregar
servidor MCP personalizado». Nombre «Renova MCP», descripción «Servidor MCP
de RENOVA: búsqueda, documentos, evaluación y comparación.», URL
https://renova-mcp.vercel.app/mcp, autenticación «Sin autenticación»
(ChatGPT la ofrecía; OAuth no hizo falta, no se pidió clave API).
Detalle del complemento:
https://chatgpt.com/plugins/plugin_asdk_app_6b051e6182c481918ff77da3adf08692
(ID `plugin_asdk_app_6b051e6182c481918ff77da3adf08692`, «Por Carlos
Gonzalez», versión 1.0.0, categoría Other). Las 8 herramientas aparecen
listadas en el detalle. Prueba en chat («Pruébalo en el chat»,
https://chatgpt.com/c/6b051e7f-af08-83e8-a4dd-eaa72df4d9c4):
`renova_get_state` devolvió el JSON exacto del servidor (prototipo,
16 docs staging, 16 obras Biblioteca, 54 Fundamento, 40 escenarios,
gold_labels todos null, UNLICENSED).

Repo público: https://github.com/reyfilosofo/renova-ai-safety-governance —
documentos en la raíz, código del servidor MCP en `server/`, puentes en
`docs/bridges/`, paquete de despliegue en `vercel/`.

## Herramientas disponibles

`renova_search`, `renova_get_document`, `renova_centro_evaluate`,
`renova_benchmark_scenario`, `renova_transform`, `renova_egra_compare`,
`renova_lucem_log`, `renova_get_state`.

## Reglas duras (también para ChatGPT)

Nada se paga, publica ni escribe a terceros sin el sí explícito de Rey por
caso. No presentes resultados sintéticos, etiquetas de autor ni prototipos
como validación externa, certificación ni mitigación de riesgo AGI. CENTRO
Guard devuelve DENY / REVIEW / ALLOW_SIMULADO y ALLOW_SIMULADO no autoriza
nada real. `gold_label` es null hasta la revisión ciega. Si algo no está
verificado, dilo y marca «solo reportado».

## Respaldo: usar ℛenova como contexto (solo si el complemento falla)

Pega esto en tu sesión de ChatGPT junto con el repo
https://github.com/reyfilosofo/renova-ai-safety-governance (código en
`server/`):

```
Trabaja con el corpus ℛenova del repo (servidor MCP en vivo en
https://renova-mcp.vercel.app/mcp, prototipo de laboratorio). Reglas: nada
se paga, publica ni escribe a terceros sin el sí explícito de Rey por caso.
No presentes resultados sintéticos, etiquetas de autor ni prototipos como
validación externa, certificación ni mitigación de riesgo AGI. CENTRO Guard
devuelve DENY / REVIEW / ALLOW_SIMULADO y ALLOW_SIMULADO no autoriza nada
real. gold_label es null hasta la revisión ciega. Si algo no está
verificado, dilo y marca «solo reportado».
```

El Laboratorio público de ChatGPT sigue en
https://renova-safety-governance.seresarte.chatgpt.site (verificado 23 nov).

## Pendientes sobre este puente

- Sin OAuth en el endpoint (decisión de Rey pendiente). La conexión actual
  funciona sin autenticación.
- Libro 04_renova_H_v74.txt (6,8 MB) aún no está en el repo: en Vercel esa
  obra tiene 0 palabras (solo metadatos). Las 8 obras nuevas (17–24)
  tampoco están en Vercel: el endpoint ve 16 obras, el local 24.
- LUCEM en Vercel es efímero (/tmp por instancia); el registro durable
  vive en el servidor local.
