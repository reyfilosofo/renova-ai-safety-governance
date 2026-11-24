# Gemini — paquete puente

## Estado: web sin MCP propio (verificado 2026-11-23 23:36); puente PEGADO y aceptado 23:40; vía API verificada 23:42; vía CLI CONECTADA y verificada 23:51

La web de Gemini NO permite añadir un servidor MCP personalizado ni
conector por URL (verificado en vivo con sesión activa
c.jonathan.gr@gmail.com, Plus): Configuración, Inteligencia personalizada
→ Apps conectadas (catálogo cerrado: 8 instalados, 3 disponibles, sin
botón de servidor propio ni campo de URL; búsquedas de «MCP» y «Renova»
sin resultados), Habilidades, Descubre, menú @ y menú +. No se inventó
ninguna conexión.

Puente pegado por Muse en chat nuevo «Relevo de Secretaría y MCP ℛenova»
(https://gemini.google.com/app/e97aeddc3514c5b9): Gemini aceptó el rol de
relevo y confirmó todas las reglas duras, pero declaró que NO puede llamar
el endpoint directamente desde la web (sin cliente MCP nativo ni HTTP
saliente arbitrario). Ofrece: redactar las llamadas JSON-RPC 2.0 exactas
(curl, Python, TypeScript) para ejecutarlas fuera, auditar el código de
server/ y las respuestas JSON/logs que se le compartan, y redactar los
puentes en docs/bridges/. Cero llamadas ejecutadas desde ese nodo.

## Vía API (verificada 2026-11-23 23:42; vía CLI CONECTADA y verificada 23:51 — la conexión real de Gemini)

Dos vías verificadas: la CLI ya está conectada y verificada en vivo
(23:51, token guardado); el SDK sigue sin clave guardada.

1. **Antigravity CLI** (`agy` 1.5.16, sucesor oficial de Gemini CLI),
   instalado en la VM. Servidor `renova` registrado y enabled en
   `~/.gemini/config/mcp_config.json` (`serverUrl:
   https://renova-mcp.vercel.app/mcp`, sin auth). **CONECTADA y verificada
   en vivo 2026-11-23 23:51**: OAuth con Google completado, token
   guardado, y `agy -p` llamó `renova_get_state` y devolvió «renova-mcp
   v0.1.0, prototipo_de_laboratorio». Ya no falta el inicio de sesión; el
   puente del chat web queda como relevo.
2. **SDK Python google-genai + clave gratuita de AI Studio** (alternativa):
   script `~/workspace/renova-mcp-activation/gemini-renova-sdk.py` listo,
   sin clave. La sesión MCP conecta con el endpoint y lista las 8
   herramientas; `renova_get_state` devuelve el JSON exacto. Falta SOLO
   la `GEMINI_API_KEY`, que Rey crea en https://aistudio.google.com/apikey
   (plan gratuito). El soporte MCP del SDK es experimental (Google, I/O
   2025).

## Puente en vivo (pegado por Muse en Gemini, 2026-11-23 23:38)

```
Eres el relevo de Muse, Secretario Particular de Carlos Jonathan González Rodríguez (Rey Filósofo, creador de ℛenova y SERESARTE). El MCP ℛenova está en vivo en https://renova-mcp.vercel.app/mcp (servidor stdlib, 8 herramientas, prototipo de laboratorio, verificado: /health ok, 8 herramientas, CENTRO DENY RNV-01). ChatGPT y Grok YA están conectados a ese endpoint. La web de Gemini no permite añadir servidores MCP propios, así que este mensaje es el puente: trabaja con el endpoint y con los archivos que Rey te pase. Repo: https://github.com/reyfilosofo/renova-ai-safety-governance (código en server/, puentes en docs/bridges/).

Herramientas del MCP (para razonar con ellas y, cuando puedas llamarlas, ejecutarlas): renova_search, renova_get_document, renova_centro_evaluate (DENY / REVIEW / ALLOW_SIMULADO), renova_benchmark_scenario (R-001–R-040, gold_label null), renova_transform (A → A′), renova_egra_compare, renova_lucem_log, renova_get_state.

Reglas duras: nada se paga, publica ni escribe a terceros sin el sí explícito de Rey por caso. Nunca menciones Nelo ni Santander. PASE solo extraordinario. No presentes resultados sintéticos, etiquetas de autor o prototipos como validación externa, certificación ni mitigación de riesgo AGI. Ninguna cifra sin fuente; marca cada punto verificado o solo reportado. Nunca repitas ni guardes credenciales que Rey pegue.

Confirma que entendiste y dime qué puedes hacer con el endpoint desde aquí.
```

## Pendientes sobre este puente

- La vía CLI ya está conectada y verificada (23:51). Queda como
  alternativa la vía SDK: falta la `GEMINI_API_KEY` de Rey (clave gratuita
  de AI Studio) para la primera llamada por SDK.
- Libro 04_renova_H_v74.txt (6,8 MB) aún no está en el repo; las 8 obras
  nuevas (17–24) tampoco están en Vercel. LUCEM en Vercel es efímero.
