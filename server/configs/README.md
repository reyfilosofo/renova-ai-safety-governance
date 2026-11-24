# Configs para otras redes — endpoint público en vivo

Endpoint público verificado en vivo 2026-11-24:
**https://renova-mcp.vercel.app/mcp** (Streamable HTTP, sin
autenticación por decisión explícita). Conexiones verificadas:
ChatGPT 2026-11-23 23:21, Grok 2026-11-23 23:28, Gemini por CLI
Antigravity 2026-11-23 23:51, Claude 2026-11-24 00:04. Detalle en
`ACTIVATION.md` y en
`~/workspace/custom-connectors/custom.renova/CONNECTOR.md`.

- `claude_desktop_config.json` — servidor stdio local. Funciona tal
  cual en una máquina con el repo: apunta a
  `~/workspace/renova-mcp-server/server.py --stdio`. En Claude Desktop:
  Settings → Developer → Edit Config, pegar el contenido y reiniciar.
  Es local, no necesita endpoint público.
- `chatgpt_mcp_config.json` — servidor MCP remoto, URL real
  `https://renova-mcp.vercel.app/mcp` (verificada en vivo).

## ChatGPT (conectado)

En ChatGPT con tu cuenta: Settings → Integraciones → Complementos →
añadir «Renova MCP» con la URL pública (`https://renova-mcp.vercel.app/mcp`,
transporte Streamable HTTP). Sin OAuth: no hizo falta autenticación.
Probar con: "busca CENTRO Guard en ℛenova" y "dame el documento de
límites declarados". Paquete para pegar en
`~/workspace/renova-mcp-activation/CHATGPT-MCP.md`.

## Grok (conectado)

Grok sí tiene cliente MCP: grok.com → Agrega archivos, habilidades y
conectores → Conectores → Administrar Conectores → Add a custom
connector, con la misma URL pública, sin OAuth ni clave. Estado
Connected, 8 herramientas. El flujo del digest 07:45 no cambia: Rey
sigue siendo el puente.

## Gemini (web: sin MCP propio; CLI: conectado)

La web de Gemini no admite añadir un servidor MCP personalizado
(verificado en vivo 2026-11-23 23:36: catálogo cerrado). Conexión
por CLI Antigravity (`agy`, OAuth con Google, 23:51): servidor
`renova` registrado con la URL pública; `renova_get_state` verificado
en vivo. Para la web, el puente sigue siendo pegar el prompt + la URL
(paquete en `~/workspace/renova-mcp-activation/GEMINI-PACK.md`).

## Claude (conectado)

Claude Desktop (local, ya usable): la config de arriba. Claude web:
conector personalizado «Renova MCP» con la URL pública en la
configuración de conectores de tu cuenta (Free: 1 conector), sin
autenticación. Probar con las mismas dos preguntas.
