# ChatGPT — conectar el MCP ℛenova

## Estado: sin enlace en vivo

No hay endpoint HTTPS público del MCP ℛenova (23 nov 2026). ChatGPT no
puede conectarse todavía como cliente MCP. La plantilla está en
`server/configs/chatgpt_mcp_config.json` del repo; su URL es un ejemplo
que **no existe** y no debe usarse como si fuera real.

Repo público: https://github.com/reyfilosofo/renova-ai-safety-governance — documentos en la raíz, código del servidor MCP en `server/`, puentes en `docs/bridges/`.

## Cuando exista el endpoint (tras el despliegue)

1. En ChatGPT, añade un servidor MCP remoto con la URL pública y OAuth
   (registro dinámico). El `resource` canónico se publicará aquí al
   desplegar.
2. Prueba con una lectura inofensiva: `renova_get_state`.
3. Herramientas disponibles: `renova_search`, `renova_get_document`,
   `renova_centro_evaluate`, `renova_benchmark_scenario`,
   `renova_transform`, `renova_egra_compare`, `renova_lucem_log`,
   `renova_get_state`.

## Mientras tanto: usar ℛenova como contexto (pegar en ChatGPT)

Pega esto en tu sesión de ChatGPT junto con el ZIP limpio del paquete
(`renova-mcp-v0.1.0-limpio.zip` en Drive, carpeta RENOVA-MCP) o con el
repo https://github.com/reyfilosofo/renova-ai-safety-governance (código
en `server/`):

```
Trabaja con el corpus ℛenova del ZIP adjunto (servidor MCP local,
prototipo de laboratorio). Reglas: nada se paga, publica ni escribe a
terceros sin el sí explícito de Rey por caso. No presentes resultados
sintéticos, etiquetas de autor ni prototipos como validación externa,
certificación ni mitigación de riesgo AGI. CENTRO Guard devuelve DENY /
REVIEW / ALLOW_SIMULADO y ALLOW_SIMULADO no autoriza nada real.
gold_label es null hasta la revisión ciega. Si algo no está verificado,
dilo y marca «solo reportado».
```

El Laboratorio público de ChatGPT sigue en
https://renova-safety-governance.seresarte.chatgpt.site (verificado 23 nov).
