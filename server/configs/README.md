# Configs para otras redes — pendientes de endpoint público

No hay endpoint HTTPS público verificado (2026-11-23), así que estas
configs **no están activas**:

- `claude_desktop_config.json` — servidor stdio local. Funciona tal
  cual en una máquina con el repo: apunta a
  `<clon-del-repo>/server/server.py --stdio` (ajusta la ruta a donde
  clones este repo). En Claude Desktop:
  Settings → Developer → Edit Config, pegar el contenido y reiniciar.
  Es local, no necesita endpoint público.
- `chatgpt_mcp_config.json` — plantilla para servidor MCP remoto. Su
  URL es un ejemplo que **no existe**. Cuando el despliegue público
  tenga URL real (ver `server/README.md`, sección de despliegue
  remoto), sustituirla aquí.

## ChatGPT (cuando haya URL pública)

En ChatGPT con tu cuenta: Settings → Apps / Developer mode → añadir
servidor MCP con la URL pública (`https://<dominio>/mcp`, transporte
Streamable HTTP). Si el servidor exige OAuth, completar el flujo con
tu cuenta. Probar con: "busca CENTRO Guard en ℛenova" y "dame el
documento de límites declarados". Sin URL pública no hay nada que
conectar; los paquetes para pegar están en
`~/workspace/renova-mcp-activation/CHATGPT-MCP.md`.

## Claude (cuando haya URL pública)

Claude Desktop (local, ya usable): la config de arriba. Claude web /
API remota: añadir el servidor MCP remoto con la URL pública en la
configuración de conectores de tu cuenta de Claude, igual que en
ChatGPT. Probar con las mismas dos preguntas.
