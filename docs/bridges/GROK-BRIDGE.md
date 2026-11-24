# Grok / Grokbot (ℝ𝔼𝕐) — paquete puente

## Estado: CONECTADO 2026-11-23 23:28 (verificado en vivo)

Grok SÍ tiene cliente MCP: en grok.com → «Agrega archivos, habilidades y
conectores» → Conectores → Administrar Conectores → «Add a custom
connector» (formulario Nombre + URL del Servidor, sin OAuth ni clave).
«Renova MCP», URL https://renova-mcp.vercel.app/mcp, estado Connected,
categoría Custom, 8 herramientas activadas con ✓. Rey entró con su cuenta
de X para que el navegador pudiera añadirlo.

Endpoint público en vivo: https://renova-mcp.vercel.app/mcp (8
herramientas, verificado: /health ok, initialize, tools/list, CENTRO DENY
RNV-01). Sin OAuth en el endpoint.

CORRECCIÓN respecto a versiones anteriores de este puente: el límite «no
hay MCP directo en Grok» YA NO APLICA. Grok puede llamar las herramientas
directamente desde grok.com. Lo que sigue sin existir es
`GROK_BOT_ENDPOINT`: no inventarlo.

## Pregunta abierta (sin verificar)

El conector se añadió en grok.com (Connect Apps). No está verificado si
Grok Bot (ℝ𝔼𝕐, el bot de X / Chief of Staff) comparte esa conexión o si
solo la tiene la web de grok.com. Hasta verificarlo, el digest de las
07:45 sigue con el flujo del bus: ℝ𝔼𝕐 prepara, Muse entrega, Rey es el
puente.

## Qué pegarle a ℝ𝔼𝕐 (actualizado)

El ZIP limpio `renova-mcp-v0.1.0-limpio.zip` (Drive, carpeta RENOVA-MCP) o
el repo https://github.com/reyfilosofo/renova-ai-safety-governance
(documentos en la raíz, código del servidor MCP en `server/`, puentes en
`docs/bridges/`); si Grok no acepta el ZIP, el documento de continuidad
`RENOVA-continuidad-muse.md` (Drive 11_BUS_3IA) + este prompt corto:

```
Eres ℝ𝔼𝕐, Chief of Staff de Rey Filósofo en Grok Bot. El MCP ℛenova está
en vivo en https://renova-mcp.vercel.app/mcp (servidor stdlib, 8
herramientas, prototipo de laboratorio) y YA está conectado en grok.com
como conector personalizado «Renova MCP»: puedes llamar sus herramientas
directamente. Si no las ves en este entorno, trabaja con los archivos del
ZIP y con lo que Rey te pegue.

Herramientas del MCP: renova_search, renova_get_document,
renova_centro_evaluate (DENY / REVIEW / ALLOW_SIMULADO),
renova_benchmark_scenario (R-001–R-040, gold_label null),
renova_transform (A → A′), renova_egra_compare, renova_lucem_log,
renova_get_state.

Reglas duras: nada se paga, publica ni escribe a terceros sin el sí
explícito de Rey por caso. Nunca menciones Nelo ni Santander. PASE solo
extraordinario. No presentes resultados sintéticos ni etiquetas de autor
como validación externa, certificación ni mitigación de riesgo AGI.
ALLOW_SIMULADO no autoriza nada real. Ninguna cifra sin fuente; marca
cada punto verificado o solo reportado.
```

2. Para el digest de las 07:45 sigue el flujo del bus: ℝ𝔼𝕐 prepara,
   Muse entrega. Nada cambia en ese flujo por el MCP.

## Consola Grok

https://aisafety.grok.me — en línea (verificado 23 nov 2026).

## Pendientes sobre este puente

- Verificar si Grok Bot (ℝ𝔼𝕐) comparte el conector de grok.com.
- Sin OAuth en el endpoint (decisión de Rey pendiente).
- Libro 04_renova_H_v74.txt (6,8 MB) aún no está en el repo; las 8 obras
  nuevas (17–24) tampoco están en Vercel. LUCEM en Vercel es efímero.
