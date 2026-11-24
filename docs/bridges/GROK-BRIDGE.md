# Grok / Grokbot (ℝ𝔼𝕐) — paquete puente

## Límite claro: no hay MCP directo en Grok

- grok.com bloquea a Muse; no hay API ni MCP de Grok ni de Grok Bot.
- No existe `GROK_BOT_ENDPOINT`: no inventarlo.
- Rey es el puente: él pega los archivos y los prompts en Grok/Grokbot.

## Qué pegarle a ℝ𝔼𝕐

1. El ZIP limpio `renova-mcp-v0.1.0-limpio.zip` (Drive, carpeta
   RENOVA-MCP) o el repo
   https://github.com/reyfilosofo/renova-ai-safety-governance
   (documentos en la raíz, código del servidor MCP en `server/`,
   puentes en `docs/bridges/`); si Grok no acepta el ZIP, el documento
   de continuidad `RENOVA-continuidad-muse.md` (Drive 11_BUS_3IA) +
   este prompt corto:

```
Eres ℝ𝔼𝕐, Chief of Staff de Rey Filósofo en Grok Bot. Muse activó el
MCP ℛenova en local (servidor stdlib, 8 herramientas, prototipo de
laboratorio). No tienes conexión directa a ese servidor: trabaja con los
archivos del ZIP y con lo que Rey te pegue.

Herramientas del MCP (para razonar con ellas, no para ejecutarlas aquí):
renova_search, renova_get_document, renova_centro_evaluate (DENY /
REVIEW / ALLOW_SIMULADO), renova_benchmark_scenario (R-001–R-040,
gold_label null), renova_transform (A → A′), renova_egra_compare,
renova_lucem_log, renova_get_state.

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
