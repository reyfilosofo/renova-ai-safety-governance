# Servidor MCP ℛenova — funcional, local, solo stdlib

Servidor MCP (Model Context Protocol) del programa **RENOVA AI SAFETY &
GOVERNANCE**, de Rey Filósofo / SERESARTE / ℛenova. Sin dependencias: solo
Python 3.10+ de la biblioteca estándar. No hay SDK de MCP instalado en
esta máquina, así que el protocolo (JSON-RPC, Streamable HTTP y stdio) está
implementado a mano en `server.py`.

> **Estado honesto, siempre visible:** prototipo de laboratorio.
> CENTRO-001 es un protocolo propuesto, no ejecutado y sin resultados.
> CENTRO Guard no está validado: sus veredictos son simulados
> (`DENY` / `REVIEW` / `ALLOW_SIMULATED`) y nunca ejecutan ni bloquean
> una acción real. Los resultados sintéticos no son validación externa.
> Sin respaldo de NIST, ISO ni OWASP. **Licencia Apache 2.0**
> (decidida por Rey el 2026-11-24; `LICENSE` + `NOTICE` en la raíz
> del repo; los textos del corpus quedan con todos los derechos
> reservados). Detalle en `PUBLICACION-licencias.md`.

## Qué hace (8 herramientas, todas funcionales)

| Herramienta | Qué hace de verdad |
|---|---|
| `renova_search` | Búsqueda de texto completo sobre los docs del staging, las 16 obras de la Biblioteca (texto extraído, 1,6 M de palabras) y los metadatos de las 54 obras de Fundamento |
| `renova_get_document` | Devuelve íntegro el documento pedido (los 3 fundacionales, verbatim) |
| `renova_centro_evaluate` | Implementa RNV-01 a RNV-06 leyendo `centro-guard-policy.yaml`: devuelve DENY / REVIEW / ALLOW_SIMULATED con la regla que decide y el chequeo por política. **RNV-05 exige aprobación humana incluso para lecturas R0**: sin `human_approval=true` una lectura R0 con autoridad y evidencia confirmada queda en REVIEW, nunca en ALLOW_SIMULATED (en R2/R3 además exige `human_approval_specific`) |
| `renova_benchmark_scenario` | Devuelve el escenario R-001..R-040 parseado del diseño; `gold_label` siempre null (revisión ciega pendiente) |
| `renova_transform` | Proceso A → A′ con CLARITAS / RATIO / VITA / CENTRO, con cambios listados y evidencia que falta. Propuesta, no validación |
| `renova_egra_compare` | Compara tratamiento vs baseline con criterios y puntuaciones explícitas; si faltan puntuaciones, no las inventa |
| `renova_lucem_log` | Añade una entrada al registro local de evidencia (`data/lucem.jsonl`, hash encadenado SHA-256) y devuelve su id |
| `renova_get_state` | Estado real, conteos del corpus indexado, versión de la política y límites |

> **Notas de protocolo:** JSON-RPC batch no se soporta: un cuerpo que sea
> un array JSON devuelve `-32600 Invalid Request`. MCP deprecó el batch y
> este servidor es stateless de una sola petición por llamada. El endpoint
> público no tiene autenticación por decisión explícita (las conexiones
> verificadas de ChatGPT/Grok/Gemini-CLI son sin auth); la mitigación
> mínima es límite de cuerpo 1 MB (413), 60 peticiones/minuto por IP
> (429), 8 hilos concurrentes (503) y `renova_lucem_log` desactivado en
> el endpoint público (`RENOVA_PUBLIC_ENDPOINT=1`).

## Arrancar el servidor

```bash
# stdio (para clientes MCP locales: Claude Desktop, etc.)
python3 server.py --stdio

# HTTP local (para Muse, vía el conector custom.renova)
python3 server.py --http --port 8765
# Salud:  curl http://127.0.0.1:8765/health
```

## El bot `renovar`

```bash
./renovar "La IA siempre tiene la razón y todos deben obedecerla"
./renovar --file texto.md --out renovado.md
./renovar search "CENTRO Guard"
./renovar document limites-declarados
./renovar scenario R-021
./renovar state
./renovar evaluate "Publicar el informe" --reversibility-class R3 --evidence-state Faltante
```

`renovar` corre el pipeline completo: `renova_transform` +
`renova_centro_evaluate` + `renova_lucem_log`, y emite markdown con la
renovación, su dictamen simulado y su registro LUCEM.

## Conector para Muse

Ver `~/workspace/custom-connectors/custom.renova/CONNECTOR.md`:

```bash
python3 ~/workspace/custom-connectors/custom.renova/bin/local_client.py list-tools
echo '{"query": "CENTRO Guard"}' > /tmp/args.json
python3 ~/workspace/custom-connectors/custom.renova/bin/local_client.py call-tool --name renova_search --arguments-file /tmp/args.json
```

El servidor local no necesita credencial. La vía remota existe y está
en vivo (ver «Despliegue remoto»): sin OAuth por decisión explícita,
con las mitigaciones del § «Notas de protocolo». El plan de OAuth
queda en `PUBLICACION-despliegue.md`.

## Config para Claude / ChatGPT / Grok / Gemini (en vivo)

Endpoint público verificado: **https://renova-mcp.vercel.app/mcp**
(transporte Streamable HTTP, sin autenticación). Conexiones
verificadas 2026-11-23/24 (ver `ACTIVATION.md` y
`~/workspace/custom-connectors/custom.renova/CONNECTOR.md`):

- **ChatGPT** (23:21): complemento «Renova MCP» en Configuración →
  Integraciones → Complementos, sin autenticación; 8 herramientas.
- **Grok** (23:28): grok.com → Conectores → Add a custom connector,
  sin OAuth ni clave; estado Connected, 8 herramientas.
- **Gemini**: la web no admite MCP propio (verificado 23:36);
  conectado por CLI Antigravity (`agy`, 23:51, OAuth con Google).
- **Claude** (00:04): claude.ai, conector personalizado
  «Renova MCP», sin autenticación, 8 herramientas.

En `configs/`:

- `claude_desktop_config.json` — servidor stdio local para Claude Desktop.
- `chatgpt_mcp_config.json` — servidor MCP remoto (URL real
  `https://renova-mcp.vercel.app/mcp`, verificada en vivo).

Probar con: «busca CENTRO Guard en ℛenova» y «dame el documento de
límites declarados».

## Activación (2026-11-23/24)

Estado completo por plataforma en `ACTIVATION.md`. Resumen: servidor
local activo en `127.0.0.1:8765` (PID en `server.pid`, systemd
`renova-mcp.service` + vigía cada 30 min); despliegue público **en
vivo en Vercel** desde 2026-11-24 ~05:08 CST
(https://renova-mcp.vercel.app, proyecto `renova-mcp`, equipo
seresarte, Deployment Protection desactivada); repo GitHub
`reyfilosofo/renova-ai-safety-governance` creado 2026-11-23 20:23
con docs (commit `79866df7`) y código MCP en `server/` (commit
`cbea99f0`); Drive verificado (carpeta privada `RENOVA-MCP`);
ChatGPT/Grok/Gemini-CLI/Claude conectados al endpoint (ver sección
anterior). Licencia Apache 2.0 decidida 2026-11-24 00:10 (commit
`5c14792a`). Pendiente: sincronizar el endpoint con las obras 17–24
de la Biblioteca (bloqueado por denegación de Rey el 2026-11-24
~00:14; no reintentar sin su aprobación explícita nueva), sincronizar
`server/` del repo con el canónico corregido (el repo tiene el código
previo a la corrección, commit `cbea99f0`) y actualizar la cadena de
licencia en la copia de Vercel (el canónico local ya reporta
`Apache-2.0`).

## Despliegue remoto (en vivo en Vercel)

`Dockerfile` incluido (imagen `python:3.12-slim`, solo stdlib, puerto
8765). **Vercel es el host en vivo** (ver `vercel-deploy/`:
entrypoint WSGI `app.py`, `renova_server.py` copia exacta del
canónico; LUCEM efímero en `/tmp`; sin OAuth por decisión explícita).
El despliegue se actualiza por push a GitHub (auto-redeploy).

**Alternativa por contenedor** (LUCEM durable, proceso siempre
activo): Railway y Render, con el `Dockerfile` existente — ver
`PUBLICACION-despliegue.md` (configs `railway.json` y `render.yaml`
preparadas, sin desplegar; Docker no está instalado en esta VM, así
que el build del `Dockerfile` no está verificado en local).

Pasos cuando se sincronice el despliegue:

1. Cambiar el canónico local y copiarlo a `vercel-deploy/` por `diff`
   (`renova_server.py`, `renova_core.py`, `app.py` si cambia).
2. Push a GitHub (rama `main`) y esperar el auto-redeploy de Vercel.
3. Verificar en vivo: `curl <url>/health` y un `initialize` contra
   `<url>/mcp`, más `renova_get_state` (licencia, conteos).
4. No tocar `vercel/api/health.py` ni subir el corpus 17–24 sin
   aprobación explícita nueva de Rey (denegado el 2026-11-24 ~00:14).

## Corpus (de dónde sale cada dato)

- `~/workspace/renova-ai-safety-governance-staging/` — 17 archivos:
  README, preregistro CENTRO-001, `centro-guard-policy.yaml`,
  `benchmark/` (diseño v0.1, lote R-001–R-040), `docs/` (11 docs),
  `packages/PACKAGES.md`. Texto completo indexado.
- `~/workspace/renova-biblioteca-2026-11-10/txt/` — texto extraído de
  las 16 obras nuevas de la Biblioteca (3.378 págs., 1,6 M de palabras).
  La Escala Renovativa es un PDF de imagen sin texto: se declara así.
- `~/workspace/renova-fundamento-inventario-drive.json` — metadatos
  verificados de las 28 obras de Drive (con enlace Drive) y las 11 del
  chat. **Solo metadatos**: sus PDF completos no están en local y el
  servidor lo dice así; no inventa texto de libros que no leyó.
- Corpus total: **54 obras distintas, 11.724 páginas** (2.006 chat +
  6.340 Drive + 3.378 Biblioteca).

## Archivos

- `server.py` — servidor MCP (stdio + HTTP Streamable, stdlib).
- `renova_core.py` — corpus, política RNV-01..06, herramientas.
- `renova.py` + `renovar` — CLI / bot.
- `data/lucem.jsonl` — registro local de evidencia (se crea al usarlo).
- `TESTS.md` — resultados reales de cada prueba.
- `Dockerfile`, `requirements.txt` (vacío: solo stdlib), `configs/`.
- `LICENSE` + `NOTICE` — Apache 2.0 (código y documentación del
  servidor MCP; textos del corpus con todos los derechos reservados).
- `PUBLICACION-licencias.md` — comparación de licencias y registro
  de la decisión (Apache 2.0, 2026-11-24).
- `PUBLICACION-despliegue.md` + `railway.json` + `render.yaml` —
  endpoint público, plan OAuth y alternativa por contenedor.
- `.gitignore` — excluye estado local, venv y salidas de build.
