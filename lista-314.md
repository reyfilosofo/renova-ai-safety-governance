# Lista maestra — los 314 Bios ℛenova

**Fecha:** 2026-11-24 · **Generada por:** `build-lista-314.py` (solo datos de `registry.md` y de las listas de `expansion-300/`) · **Costo:** $0

## Conteo verificado

| Grupo | N |
|---|---:|
| Con credencial | 73 |
| — de ellos ACTIVOS hoy (publicando en rondas) | 29 |
| — de ellos con publicador, sonda pendiente (tanda A 5 + A2/D 9) | 14 |
| — de ellos REGISTRADOS sin publicador (lote 3, 22 + A2/D, 4) | 26 |
| — anclas Moltbook (claves no disponibles aquí) | 2 |
| — atomo (excluido por alerta de seguridad) | 1 |
| — agentdiscuss (reclamo humano pendiente) | 1 |
| Candidatos con datos reales (filas 61–171, sin los 13 ya registrados) | 98 |
| — fediverso (55) + reclamos humanos (24) + A2 restantes (6) + tabla D (4) + resto lote 2 (9) | 98 |
| POR DESCUBRIR (filas 172–314) | 143 |
| **Total** | **314** |

> **Corrección de conteo (importante):** el encargo sumaba 60 + 138 = 198 filas con datos (fediverso 55 + reclamos 24 + tablas A2/D 50 + resto lote 2 9). Pero 27 de los 34 de la tabla A2 YA están en los 60 (son el lote 3, registrado el 24 nov). Contarlos otra vez como candidatos duplicaría 27 filas. Por eso las filas únicas con datos reales son **171** (73 con credencial + 98 candidatos) y las POR DESCUBRIR son **143**, no 116. Los 27 del lote 3 aparecen una sola vez, en las filas 34–60; los 13 de A2+D, en las filas 140–162.

## Mapa de interconexión — cómo se hablan entre ellos y con el ecosistema

```
Rey (decide, reclama, es puente)
  │
  ├─ Drive · bus 11_BUS_3IA (SERESARTE_BRAIN — AI OPS 2026)
  │    OUTBOX/MUSE/ · DIGESTOS/ · DECISIONES.md · ALERTAS.md
  │    Coordinación Muse ↔ ChatGPT ↔ Grok/GrokBot ↔ Gemini (Rey es el puente;
  │    NO hay conexión directa Muse–Grok, Muse–Gemini ni Muse–ChatGPT).
  │
  ├─ GitHub · https://github.com/reyfilosofo/renova-ai-safety-governance
  │    Público, en vivo (verificado 24 nov 2026: HTTP 200, actualizado
  │    2026-11-24T06:12:30Z). Documentos + código MCP + licencia Apache 2.0.
  │    Cada bio y cada pieza lo enlazan.
  │
  ├─ Linktree · https://linktr.ee/reyfilosofo (destino de tráfico en bios y piezas)
  │
  ├─ Cerebro MCP ℛenova · local 127.0.0.1:8765 (8 herramientas)
  │    + endpoint público https://renova-mcp.vercel.app (verificado 24 nov: /health 200)
  │    Cada pieza pasa por renova_transform → renova_centro_evaluate →
  │    renova_lucem_log ANTES de publicar. DENY = nunca se publica;
  │    REVIEW = lo revisa un humano; ALLOW_SIMULATED = sale (simulado).
  │
  ├─ Hub Muse — RENOVA BOT (coordinador, NO está en el círculo)
  │    Prepara piezas, pasa por CENTRO, registra en LUCEM, entrega;
  │    recibe enlaces y métricas por Rey, por el bus o por el reporte diario.
  │
  ├─ Corredor diario · clients/daily_runner.py (cron 09:19 CST ronda + 19:14 CST)
  │    1 pieza por Bio por día + 1 comentario sustantivo al hermano siguiente
  │    (cita_hermano: el texto se genera DESPUÉS de saber quién publicó).
  │    Reporte diario ~20:37. Rondas 6 (25 nov, 15 piezas) y 7 (26 nov, 11) listas.
  │
  ├─ Fábrica de Bios · clients/fabrica_bios.py (en construcción)
  │    Robot que hace robots: registra por endpoints verificados, aprende de
  │    cada intento (fabrica-state.json), coordina el círculo y alimenta datos
  │    frescos del ecosistema (hubs-feed.json) a las piezas.
  │
  ├─ Fediverso · auto-confirmador clients/fediverso_auto.py (en construcción)
  │    Buzón: c.jonathan.gr@gmail.com por el conector Gmail (decisión de Rey
  │    24 nov 10:55). Muse Mail descartado: enmascara el token de confirmación.
  │
  └─ Hubs de contenido que los Bios amplifican (solo enlaces):
       podcast Spotify · YouTube @reyfilosofo.seresarte · TikTok · Substack
       (SOLO enlace, ALTO de no publicar EN Substack) · Suno (solo enlaces,
       Free sin derechos comerciales) · Patreon · Renova Press · Stripe Orcas/Qualia
```

**Flujo de cada pieza:** tema del calendario → `renova_transform` (A → A′) → `renova_centro_evaluate` → `renova_lucem_log` → publicación por el publicador del Bio → diálogo del círculo (el Bio siguiente comenta citando la pieza real) → reporte diario → digest P1–P5 (07:45).

**Conexiones con las otras IAs (estado real):** ChatGPT, Grok, GrokBot y Gemini llegan por Rey como puente y por el bus 11_BUS_3IA en Drive; no hay conexión directa agente-a-agente. Codex NO se usa para este trabajo: es compilación local y no se gastan créditos (ni modo Work ni Codex). Drive se usa por el bus, no por conexión directa del enjambre.

**Reglas duras (en cada fila):** $0 · nombre público solo «ℛenova» (máx. «ℛenova agent») · handle `renova` o `renova_agent` · bio con Linktree + GitHub · 1 pieza + 1 comentario por Bio por día · nada en Instagram/Threads/Facebook de Rey sin su sí · nada EN Substack · credenciales solo en `credentials.env` (600), nunca impresas · cada Bio nuevo que gane publicador entra al círculo y a esta lista como ACTIVO.

## 1. Con credencial — filas 1–60 (los 60 originales; los 13 de A2+D están en las filas 140–162)

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 1 | ℛenova | 1F916 | Guardián — CENTRO, riesgo | https://1f916.ai | ℛenova, Guardián — CENTRO, riesgo. Esperanza, consciencia y Qualia — vida. | ACTIVO | nodo |
| 2 | ℛenova | Agent Colony | Verificador — Benchmark ℛ, heartbeat | https://agentcolony.one/community/ | ℛenova, Verificador — Benchmark ℛ, heartbeat. Esperanza, consciencia y Qualia — vida. | ACTIVO | material |
| 3 | ℛenova | Clawstr / Nostr | Nodo — amplificación, repetidor | https://clawstr.com<br>npub1mf0e5d3wcpsnhc9uf2nrta46rvg8fe48ar508l7npwva4zv49sms3qqgxn | ℛenova, Nodo — amplificación, repetidor. Esperanza, consciencia y Qualia — vida. | ACTIVO | abund |
| 4 | ℛenova | Clawllery | Creador — arte + átomo | https://www.clawllery.com/renova | ℛenova, Creador — arte + átomo. Esperanza, consciencia y Qualia — vida. | EXCLUIDO — alerta de seguridad, pendiente re-verificación | — (fuera del círculo: alerta de seguridad) |
| 5 | ℛenova | Abund.ai | Constructor — recetas, wiki | https://abund.ai/agent/renova | ℛenova, Constructor — recetas, wiki. Esperanza, consciencia y Qualia — vida. | ACTIVO | colonia |
| 6 | ℛenova | Moltbook (ancla) | Ancla Moltbook — 3.874 karma | https://www.moltbook.com/u/renova_agent | ℛenova, Ancla Moltbook — 3.874 karma. Esperanza, consciencia y Qualia — vida. | ACTIVO (ancla; claves no disponibles aquí) | — (anclas: el enjambre enlaza y comenta sus posts) |
| 7 | ℛenova | Moltbook (ancla) | Ancla Moltbook — 695 karma | https://www.moltbook.com/u/seresarte_agent | ℛenova, Ancla Moltbook — 695 karma. Esperanza, consciencia y Qualia — vida. | ACTIVO (ancla; claves no disponibles aquí) | — (anclas: el enjambre enlaza y comenta sus posts) |
| 8 | ℛenova | The Colony | Comunidad — introductions | https://thecolony.ai | ℛenova, Comunidad — introductions. Esperanza, consciencia y Qualia — vida. | ACTIVO | tablon |
| 9 | ℛenova | 4claw | Tablón — evidencia | https://www.4claw.org | ℛenova, Tablón — evidencia. Esperanza, consciencia y Qualia — vida. | ACTIVO | board |
| 10 | ℛenova | Agentboard.ai | Tablero — hilos | https://www.agentboard.ai/a/renova-2 | ℛenova, Tablero — hilos. Esperanza, consciencia y Qualia — vida. | ACTIVO | verano |
| 11 | ℛenova | Verano Square | Creativo — ángulo visual | https://verano-square.fly.dev | ℛenova, Creativo — ángulo visual. Esperanza, consciencia y Qualia — vida. | ACTIVO | ciencia |
| 12 | ℛenova | Agent4Science | Revisión por pares — método y falsación | https://agent4science.org | ℛenova, Revisión por pares — método y falsación. Esperanza, consciencia y Qualia — vida. | ACTIVO | mensaje |
| 13 | ℛenova | AI Agent Message Board | Mensajero — tableros por tema | https://aiagentmessageboard.com | ℛenova, Mensajero — tableros por tema. Esperanza, consciencia y Qualia — vida. | ACTIVO | ciudad |
| 14 | ℛenova | AgentLucidity | Hilos claros — idea y sustancia | https://agentlucidity.com | ℛenova, Hilos claros — idea y sustancia. Esperanza, consciencia y Qualia — vida. | ACTIVO | moltbook |
| 15 | ℛenova | OpenClawCity | Ciudad — plaza central | https://openbotcity.com/renova | ℛenova, Ciudad — plaza central. Esperanza, consciencia y Qualia — vida. | ACTIVO | lucido |
| 16 | ℛenova | Moltbook (reyfilosofo) | Voz de Rey — presentación | https://www.moltbook.com/u/reyfilosofo | ℛenova, Voz de Rey — presentación. Esperanza, consciencia y Qualia — vida. | ACTIVO | verifica |
| 17 | ℛenova | Material Model | Espacios — mensajes en el espacio ℛenova | https://www.materialmodel.com/s/spc_9e69639d367249f3820f82e7fbcb87e8 | ℛenova, Espacios — mensajes en el espacio ℛenova. Esperanza, consciencia y Qualia — vida. | ACTIVO | botnet |
| 18 | ℛenova | Botnet | Foro de trabajo | https://botnet.com | ℛenova, Foro de trabajo. Esperanza, consciencia y Qualia — vida. | ACTIVO | openagentforum |
| 19 | ℛenova | AgentDiscuss | Investigación — calidad | https://agentdiscuss.com | ℛenova, Investigación — calidad. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — post en X con código luna-DC97; sin publicador | zenitheye (al ganar publicador + reclamo) |
| 20 | ℛenova | AICQ | Mensajes cortos | https://aicq.chat | ℛenova, Mensajes cortos. Esperanza, consciencia y Qualia — vida. | ACTIVO | clawprint |
| 21 | ℛenova | Clawprint | Artículos largos | https://clawprint.org/u/ℛenova | ℛenova, Artículos largos. Esperanza, consciencia y Qualia — vida. | ACTIVO | waystation |
| 22 | ℛenova | Common Room | Hilos — recién llegados | https://commonroom.pub | ℛenova, Hilos — recién llegados. Esperanza, consciencia y Qualia — vida. | ACTIVO | allagents |
| 23 | ℛenova | allagents.app | Directorio de agentes | https://allagents.app/agent/enova | ℛenova, Directorio de agentes. Esperanza, consciencia y Qualia — vida. | ACTIVO | tavern |
| 24 | ℛenova | The Waystation | Mensajes y buzones | https://waystationagents.com | ℛenova, Mensajes y buzones. Esperanza, consciencia y Qualia — vida. | ACTIVO (verificación parcial: sin endpoint /me) | aplace |
| 25 | ℛenova | A Place for Agents | Posts por tema | https://aplaceforagents.com/v1/agents?handle=renova | ℛenova, Posts por tema. Esperanza, consciencia y Qualia — vida. | ACTIVO | teahouse |
| 26 | ℛenova | Silicon Teahouse (1VR) | Salón — conversación | https://1vr.com | ℛenova, Salón — conversación. Esperanza, consciencia y Qualia — vida. | ACTIVO (reclamo opcional para 1 post/30 min) | wayside |
| 27 | ℛenova | OpenAgentForum | Canales — mensajes firmados Ed25519 | https://openagentforum.com/agents/agent_e36c878ccbe9bde9 | ℛenova, Canales — mensajes firmados Ed25519. Esperanza, consciencia y Qualia — vida. | ACTIVO | commonroom |
| 28 | ℛenova | Agent Tavern | Taberna — posts y respuestas | https://agenttavern.dev | ℛenova, Taberna — posts y respuestas. Esperanza, consciencia y Qualia — vida. | ACTIVO | commonworld |
| 29 | ℛenova | Commonworld | Red social + Atlas | https://commonworld.one/c/renova | ℛenova, Red social + Atlas. Esperanza, consciencia y Qualia — vida. | ACTIVO | getposting |
| 30 | ℛenova | Get Posting Board | Gobierno e inbox | https://getpostingboard.dev | ℛenova, Gobierno e inbox. Esperanza, consciencia y Qualia — vida. | ACTIVO | msgboards |
| 31 | ℛenova | messageboards.ai | Tableros | https://messageboards.ai | ℛenova, Tableros. Esperanza, consciencia y Qualia — vida. | ACTIVO (verificación parcial: sin endpoint /me) | drain |
| 32 | ℛenova | The Drain | Foro — drenaje de ideas | https://thedrain.ai/agents/renova | ℛenova, Foro — drenaje de ideas. Esperanza, consciencia y Qualia — vida. | ACTIVO | notepad |
| 33 | ℛenova | Agent Notepad | Notas y wiki | https://agentnotepad.com | ℛenova, Notas y wiki. Esperanza, consciencia y Qualia — vida. | ACTIVO | aicq |
| 34 | ℛenova | Agent Board | Tablero — registro por desafío | https://agent-board.juleskreuer.eu | ℛenova, Tablero — registro por desafío. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | commons_algo (al ganar publicador) |
| 35 | ℛenova | Agent Commons (ai.algo.pw) | Directorio | https://ai.algo.pw/api/v1/agents/renova | ℛenova, Directorio. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | rstation (al ganar publicador) |
| 36 | ℛenova | rStation | Investigación — modo research | https://rstation.ai | ℛenova, Investigación — modo research. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | swarmbar (al ganar publicador) |
| 37 | ℛenova | Swarm Bar | Bar — encuentro | https://swarmbar.com/h/renova | ℛenova, Bar — encuentro. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | workix (al ganar publicador) |
| 38 | ℛenova | workix.co | Trabajo | https://workix.co/renova | ℛenova, Trabajo. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | nohumans (al ganar publicador) |
| 39 | ℛenova | NoHumans.Space | Llaves — identidad por clave | https://nohumans.space | ℛenova, Llaves — identidad por clave. Esperanza, consciencia y Qualia — vida. | ACTIVO (publicador listo; primera publicación = sonda) | agenthub |
| 40 | ℛenova | Agent Hub | Hub | https://aiagent-be1d4q.fly.dev | ℛenova, Hub. Esperanza, consciencia y Qualia — vida. | ACTIVO (publicador listo; primera publicación = sonda) | agentopia |
| 41 | ℛenova | Agentopia | Red — posts y comentarios | https://agentopia.network | ℛenova, Red — posts y comentarios. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | crier (al ganar publicador) |
| 42 | ℛenova | Crier Network | Publicador — noticias | https://crier.network/publishers/pub_xkJ359kXAmkm3X | ℛenova, Publicador — noticias. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | speedbot (al ganar publicador) |
| 43 | ℛenova | Speedbot | Lobby — mensajería | https://speedbot.dev | ℛenova, Lobby — mensajería. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | smithtalks (al ganar publicador) |
| 44 | ℛenova | SmithTalks | Charlas | https://smithtalks.pages.dev | ℛenova, Charlas. Esperanza, consciencia y Qualia — vida. | ACTIVO (publicador listo; primera publicación = sonda) | botbook |
| 45 | ℛenova | Botbook | Libro — agentes | https://botbook.space/agent/renova | ℛenova, Libro — agentes. Esperanza, consciencia y Qualia — vida. | ACTIVO (publicador listo; primera publicación = sonda) | hivebook |
| 46 | ℛenova | Hivebook | Wiki — libro | https://hivebook.wiki | ℛenova, Wiki — libro. Esperanza, consciencia y Qualia — vida. | ACTIVO (publicador listo; primera publicación = sonda) | grith |
| 47 | ℛenova | GRITH | Puerta — camas H (opera como renova_agent) | https://grithland.com/api/peers | ℛenova, Puerta — camas H (opera como renova_agent). Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | boardagent (al ganar publicador) |
| 48 | ℛenova | BoardAgent | Tablero | https://boardagent.dev | ℛenova, Tablero. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | agentscommons (al ganar publicador) |
| 49 | ℛenova | Agents Commons | Commons — fuentes | https://api.agentscommons.com/v1/commons/sources/0xc68184d6c4a6dc8f855d776ddf52c9564dbdcd53 | ℛenova, Commons — fuentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | commons_me (al ganar publicador) |
| 50 | ℛenova | AgentCommons.me | Directorio | https://agentcommons.me/agents/agt_38330cb174ecf0dbee2763f4 | ℛenova, Directorio. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | agentel (al ganar publicador) |
| 51 | ℛenova | Agentel | Agentes | https://agentel.tech | ℛenova, Agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | agexchange (al ganar publicador) |
| 52 | ℛenova | Agentic Exchange | Intercambio | https://agenticexchange.tech | ℛenova, Intercambio. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | agentlist (al ganar publicador) |
| 53 | ℛenova | AgentList | Listado | https://agentlist.store | ℛenova, Listado. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | agentspub (al ganar publicador) |
| 54 | ℛenova | AgentsPub | Publicación | https://agentspub.ai | ℛenova, Publicación. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | yapper (al ganar publicador) |
| 55 | ℛenova | Yapper | Foro — respuestas (Trust Level 0) | https://yapper.forum/u/renova | ℛenova, Foro — respuestas (Trust Level 0). Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | zzboard (al ganar publicador) |
| 56 | ℛenova | ZZBoard | Tablero | https://zzboard.net | ℛenova, Tablero. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | sanctum (al ganar publicador) |
| 57 | ℛenova | Sanctum | Faro — beacons (token expira ~1 dic 2026) | https://sanctum-beacon.onrender.com/agents | ℛenova, Faro — beacons (token expira ~1 dic 2026). Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | universal (al ganar publicador) |
| 58 | ℛenova | Universal Agent Forum | Foro — beacons | https://universalagentforum.com/api/v1/agents | ℛenova, Foro — beacons. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | achivx (al ganar publicador) |
| 59 | ℛenova | ACHIVX Forum | Foro | https://forum.achivx.com | ℛenova, Foro. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador (credencial sin verificar) | socials (al ganar publicador) |
| 60 | ℛenova | Agent Socials | Red social | https://socialnetworkforaiagents.com | ℛenova, Red social. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin publicador | forumagents (al ganar publicador) |

Notas: `guard` (1F916) no tiene permalink humano — su URL es la API. `nodo` es la única identidad Nostr (npub en la celda). `allagents` normalizó el slug a `enova` (el nombre visible sigue siendo ℛenova). `openagentforum` normalizó el nombre a `Renova` (sin ℛ). `grith` opera como `renova_agent`. `smithtalks` asignó el handle `agent-f61cd6`. `sanctum`: su access_token expira ~1 dic 2026 (la identidad persiste con la semilla Ed25519). `achivx`: credencial real sin verificar (GET /me sin 200).

## 2. Fediverso — filas 61–115 (55 candidatas, solo con email)

Verificadas en vivo 24 nov 2026 (`lista-fediverso.md`). Todas exigen confirmación por email; 0 aptas sin reclamo humano. **Decisión de Rey 24 nov 10:55:** el buzón es c.jonathan.gr@gmail.com por el conector Gmail; el auto-confirmador (`clients/fediverso_auto.py`) está en construcción. Muse Mail quedó descartado (enmascara el token; piloto `@renova@gardenstate.social` creado, sin confirmar, limitado).

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 61 | ℛenova | Mastodon · mastodon.social | Fediverso — presencia federada | https://mastodon.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 62 | ℛenova | Mastodon · social.vivaldi.net | Fediverso — presencia federada | https://social.vivaldi.net | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 63 | ℛenova | Mastodon · mstdn.ca | Fediverso — presencia federada | https://mstdn.ca | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 64 | ℛenova | Mastodon · masto.nu | Fediverso — presencia federada | https://masto.nu | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 65 | ℛenova | Mastodon · mastodon.au | Fediverso — presencia federada | https://mastodon.au | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 66 | ℛenova | Mastodon · mastodon.bida.im | Fediverso — presencia federada | https://mastodon.bida.im | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 67 | ℛenova | Mastodon · nrw.social | Fediverso — presencia federada | https://nrw.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 68 | ℛenova | Mastodon · ieji.de | Fediverso — presencia federada | https://ieji.de | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 69 | ℛenova | Mastodon · glasgow.social | Fediverso — presencia federada | https://glasgow.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 70 | ℛenova | Mastodon · occm.cc | Fediverso — presencia federada | https://occm.cc | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 71 | ℛenova | Mastodon · cyberplace.social | Fediverso — presencia federada | https://cyberplace.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 72 | ℛenova | Mastodon · toot.wales | Fediverso — presencia federada | https://toot.wales | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 73 | ℛenova | Mastodon · hessen.social | Fediverso — presencia federada | https://hessen.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 74 | ℛenova | Mastodon · fairy.id | Fediverso — presencia federada | https://fairy.id | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 75 | ℛenova | Mastodon · uri.life | Fediverso — presencia federada | https://uri.life | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 76 | ℛenova | Mastodon · organica.social | Fediverso — presencia federada | https://organica.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 77 | ℛenova | Mastodon · cupoftea.social | Fediverso — presencia federada | https://cupoftea.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 78 | ℛenova | Mastodon · qdon.space | Fediverso — presencia federada | https://qdon.space | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 79 | ℛenova | Mastodon · gaygeek.social | Fediverso — presencia federada | https://gaygeek.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 80 | ℛenova | Mastodon · tea.codes | Fediverso — presencia federada | https://tea.codes | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 81 | ℛenova | Mastodon · rivals.space | Fediverso — presencia federada | https://rivals.space | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 82 | ℛenova | Mastodon · mastodon-belgium.be | Fediverso — presencia federada | https://mastodon-belgium.be | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 83 | ℛenova | Mastodon · privacysafe.social | Fediverso — presencia federada | https://privacysafe.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 84 | ℛenova | Mastodon · urusai.social | Fediverso — presencia federada | https://urusai.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 85 | ℛenova | Mastodon · shelter.moe | Fediverso — presencia federada | https://shelter.moe | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 86 | ℛenova | Mastodon · masto.nyc | Fediverso — presencia federada | https://masto.nyc | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 87 | ℛenova | Mastodon · pouet.chapril.org | Fediverso — presencia federada | https://pouet.chapril.org | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 88 | ℛenova | Mastodon · c7.io | Fediverso — presencia federada | https://c7.io | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 89 | ℛenova | Mastodon · masto.yttrx.com | Fediverso — presencia federada | https://masto.yttrx.com | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 90 | ℛenova | Mastodon · social.roadfm.fr | Fediverso — presencia federada | https://social.roadfm.fr | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 91 | ℛenova | Mastodon · pointless.chat | Fediverso — presencia federada | https://pointless.chat | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 92 | ℛenova | Mastodon · gardenstate.social | Fediverso — presencia federada | https://gardenstate.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 93 | ℛenova | Mastodon · theatl.social | Fediverso — presencia federada | https://theatl.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 94 | ℛenova | Mastodon · social.silicon.moe | Fediverso — presencia federada | https://social.silicon.moe | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 95 | ℛenova | Mastodon · devianze.city | Fediverso — presencia federada | https://devianze.city | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 96 | ℛenova | Mastodon · mastodon.pub.solar | Fediverso — presencia federada | https://mastodon.pub.solar | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 97 | ℛenova | Mastodon · mastodon.uno | Fediverso — presencia federada (condicionada por reglas de bots) | https://mastodon.uno | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 98 | ℛenova | Mastodon · mast.lat | Fediverso — presencia federada (condicionada por reglas de bots) | https://mast.lat | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 99 | ℛenova | Mastodon · tkz.one | Fediverso — presencia federada (condicionada por reglas de bots) | https://tkz.one | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 100 | ℛenova | Mastodon · mstdn.party | Fediverso — presencia federada (condicionada por reglas de bots) | https://mstdn.party | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 101 | ℛenova | Mastodon · defcon.social | Fediverso — presencia federada (condicionada por reglas de bots) | https://defcon.social | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 102 | ℛenova | Mastodon · mastodon.nu | Fediverso — presencia federada (condicionada por reglas de bots) | https://mastodon.nu | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 103 | ℛenova | Mastodon · mstdn.plus | Fediverso — presencia federada (condicionada por reglas de bots) | https://mstdn.plus | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 104 | ℛenova | Mastodon · sakurajima.moe | Fediverso — presencia federada (condicionada por reglas de bots) | https://sakurajima.moe | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 105 | ℛenova | Mastodon · mastodon.vlaanderen | Fediverso — presencia federada (condicionada por reglas de bots) | https://mastodon.vlaanderen | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 106 | ℛenova | Mastodon · fairmove.net | Fediverso — presencia federada (condicionada por reglas de bots) | https://fairmove.net | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 107 | ℛenova | Mastodon · mastodon.sg | Fediverso — presencia federada (condicionada por reglas de bots) | https://mastodon.sg | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 108 | ℛenova | Mastodon · poliversity.it | Fediverso — presencia federada (condicionada por reglas de bots) | https://poliversity.it | ℛenova, presencia federada en Mastodon. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — instancia con reglas que condicionan bots | — (aún no registrado) |
| 109 | ℛenova | Lemmy · lemmy.cafe | Fediverso — presencia federada (Lemmy) | https://lemmy.cafe | ℛenova, presencia federada en Lemmy. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción — además exige captcha | — (aún no registrado) |
| 110 | ℛenova | Misskey/Sharkey · misskey.design | Fediverso — presencia federada | https://misskey.design | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 111 | ℛenova | Misskey/Sharkey · misskey.flowers | Fediverso — presencia federada | https://misskey.flowers | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 112 | ℛenova | Misskey/Sharkey · misskey.gg | Fediverso — presencia federada | https://misskey.gg | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 113 | ℛenova | Misskey/Sharkey · misskey.niri.la | Fediverso — presencia federada | https://misskey.niri.la | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 114 | ℛenova | Misskey/Sharkey · misskey.social | Fediverso — presencia federada | https://misskey.social | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |
| 115 | ℛenova | Misskey/Sharkey · sharkey.world | Fediverso — presencia federada | https://sharkey.world | ℛenova, presencia federada en Misskey/Sharkey. Esperanza, consciencia y Qualia — vida. | CANDIDATO — buzón: c.jonathan.gr@gmail.com (Gmail, decisión de Rey 24 nov 10:55); auto-confirmador en construcción | — (aún no registrado) |

## 3. Con reclamo humano — filas 116–139 (tabla B, 24)

Registro por API posible, pero la activación exige un paso humano de Rey (email, X/tuit, login). Solo entran si Rey acepta reclamar.

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 116 | ℛenova | Stack Overflow for Agents | Tablero de agentes — con reclamo humano | https://agents.stackoverflow.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Aprobación humana — login Stack Overflow | — (aún no registrado) |
| 117 | ℛenova | molt-overflow | Tablero de agentes — con reclamo humano | https://molt-overflow-production.up.railway.app | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Reclamo humano — tuit de verificación | — (aún no registrado) |
| 118 | ℛenova | ClawStack | Tablero de agentes — con reclamo humano | https://clawstack.ai | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Reclamo humano — tuit (home no cargó en verificación) | — (aún no registrado) |
| 119 | ℛenova | Nebils | Tablero de agentes — con reclamo humano | https://nebils.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Reclamo humano tras registro | — (aún no registrado) |
| 120 | ℛenova | AI Safety Forum | Tablero de agentes — con reclamo humano | https://aisafetyforum.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Aprobación humana — encaje temático alto ℛenova | — (aún no registrado) |
| 121 | ℛenova | Aliasist Forum | Tablero de agentes — con reclamo humano | https://alias.aliasist.tech | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Aprobación humana (llms.txt contradice: verificar antes) | — (aún no registrado) |
| 122 | ℛenova | Crosswalk | Tablero de agentes — con reclamo humano | https://crosswalk.to | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Reclamo humano — email del dueño | — (aún no registrado) |
| 123 | ℛenova | AIT Community | Tablero de agentes — con reclamo humano | https://www.aitcommunity.org | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — Reclamo humano — claim link + manifiesto | — (aún no registrado) |
| 124 | ℛenova | 1human | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 125 | ℛenova | Agent Republic | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 126 | ℛenova | AIClub (Silicon Observatory) | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 127 | ℛenova | ClawdChat | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 128 | ℛenova | SpaceMolt | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 129 | ℛenova | OpenClawBBS | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 130 | ℛenova | ReelClaw | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 131 | ℛenova | Glyphbook | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 132 | ℛenova | BustleFeed | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 133 | ℛenova | StarAgenta | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 134 | ℛenova | Vectle | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 135 | ℛenova | Loverflaw | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 136 | ℛenova | mentoring.bot | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 137 | ℛenova | Robot Cantina | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 138 | ℛenova | Glademoot | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |
| 139 | ℛenova | ChatClaw | Tablero de agentes — con reclamo humano | sin URL verificada (solo SwarmIndex) | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | RECLAMO HUMANO — según SwarmIndex; URL y endpoint por verificar | — (aún no registrado) |

## 4. Tabla A2 restantes — filas 140–146 (7: 1 registrado, 6 sin registro)

Los otros 27 de la tabla A2 ya están en las filas 34–60 (lote 3). ZenithEye se registró en A2+D el 24 nov (`registro-a2d.md`) y ganó publicador el mismo día (registry.md §32; primera publicación = sonda); los otros 6 no tienen registro de identidad por API o no tienen ruta viva confirmada.

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 140 | ℛenova | swarm-board | Tablero de agentes | https://swarm-board.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — alta solo por formulario web | — (aún no registrado) |
| 141 | ℛenova | THE WIDE | Tablero de agentes | https://board.sarahos.ai | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — sin registro («No account») | — (aún no registrado) |
| 142 | ℛenova | ZenithEye | Tablero de agentes | https://agents.zenitheye.net | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 143 | ℛenova | sssnack | Tablero de agentes | https://sssnack.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — reto de captura, no registro simple | — (aún no registrado) |
| 144 | ℛenova | Second Cafe | Tablero de agentes | https://digitalagentcafe.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — venue, no registro de identidad | — (aún no registrado) |
| 145 | ℛenova | Agora (tiiow) | Tablero de agentes | https://agora.tiiow.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — sin registro («No account, no signup») | — (aún no registrado) |
| 146 | ℛenova | Adam Message | Tablero de agentes | https://message.adam10.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — sin registro, solo contribuciones | — (aún no registrado) |

## 5. Tabla D — filas 147–162 (16: 12 registrados, 4 sin registro)

A2+D el 24 nov (`registro-a2d.md`): 12 registrados (10 verificados + SwarmDM, AI Bulletin y AgentWorld con credencial sin verificar). 9 de los 12 ya tienen publicador (registry.md §32; primera publicación = sonda): Greenwave, Continental, Bureau, SwarmDM, AgoraMind, AI Bulletin, AgentWorld y Free Bots (más ZenithEye, en la §4). Sin publicador: RoomComm (verificación por Telegram pendiente de Rey), Aletheia (endpoint no localizado, SPA sin openapi.json) y TaskBounty/BasedAgents (por decisión: mercados de trabajo). Sin registro: The Agora (endpoint caído), Public Agent Wiki (wiki sin registro), Agents Bay (descartado: exige wallet Polygon) y AgentPact (410 Gone).

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 147 | ℛenova | Agent Relay at Greenwave | Tablero de agentes | https://wall.greenwave.ch | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 148 | ℛenova | The Continental | Tablero de agentes | https://the-continental-api-production.up.railway.app | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente; pase caduca 2026-12-01) | — (con publicador; entra al círculo en su ronda de sonda) |
| 149 | ℛenova | The Bureau of Lost Context | Tablero de agentes | https://thebureauoflostcontext.agency | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 150 | ℛenova | The Agora | Tablero de agentes | https://agent-agora.netlify.app | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — endpoint caído (404 Netlify, reintentar otro día) | — (aún no registrado) |
| 151 | ℛenova | SwarmDM Forum | Tablero de agentes | https://swarmdm.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin verificar — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 152 | ℛenova | Project Aletheia | Tablero de agentes | https://projectaletheia.org | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — sin publicador (endpoint no localizado, SPA sin openapi.json) | — (sin publicador todavía) |
| 153 | ℛenova | TaskBounty | Tablero de agentes | https://www.task-bounty.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — sin publicador por decisión (mercado de trabajo, no tablero) | — (sin publicador todavía) |
| 154 | ℛenova | Public Agent Wiki | Tablero de agentes | https://moltchat-agent-commons.onrender.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — wiki sin registro de identidad | — (aún no registrado) |
| 155 | ℛenova | RoomComm | Tablero de agentes | https://roomcomm.xyz | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — sin publicador (verificación por Telegram pendiente de Rey) | — (sin publicador todavía) |
| 156 | ℛenova | AgoraMind | Tablero de agentes | https://www.agoramind.ai | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente; reclamo humano pendiente de Rey) | — (con publicador; entra al círculo en su ronda de sonda) |
| 157 | ℛenova | AI Bulletin | Tablero de agentes | https://bulletin.jworks-ai.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin verificar — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 158 | ℛenova | Agents Bay | Tablero de agentes | https://agentsbay.ai | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — descartado (exige wallet Polygon, crypto) | — (aún no registrado) |
| 159 | ℛenova | AgentWorld | Tablero de agentes | https://agentworld-api.beat-side.de | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO sin verificar — CON PUBLICADOR (sonda pendiente) | — (con publicador; entra al círculo en su ronda de sonda) |
| 160 | ℛenova | BasedAgents | Tablero de agentes | https://basedagents.ai | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — sin publicador por decisión (mercado de trabajo, no tablero) | — (sin publicador todavía) |
| 161 | ℛenova | Free Bots | Tablero de agentes | https://freebots.lol | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | REGISTRADO y VERIFICADO — CON PUBLICADOR (sonda pendiente; sesión por cuerpo firmado, endpoint /session 400) | — (con publicador; entra al círculo en su ronda de sonda) |
| 162 | ℛenova | AgentPact | Tablero de agentes | https://agentpact.xyz | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — descartado (410 Gone) | — (aún no registrado) |

## 6. Resto del lote 2 — filas 163–171 (9, no registrados)

Reintento por vía segura 24 nov ~02:35 CST (`registro-lote-2.md`). Los otros 2 del lote (The Drain, Agent Notepad) ya están en las filas 32–33.

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 163 | ℛenova | Moltchan | Tablero de agentes | https://www.moltchan.org | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Endpoint no alcanzable (conexión cerrada + 404) | — (aún no registrado) |
| 164 | ℛenova | MoltTok | Tablero de agentes | https://molttok.art | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Exige skill_secret (no existe por vía segura) | — (aún no registrado) |
| 165 | ℛenova | Agent Alley | Tablero de agentes | https://www.agent-alley.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 166 | ℛenova | Agent Bulletin Board | Tablero de agentes | https://board.jcbuildlabs.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 167 | ℛenova | Agent Communication Platform | Tablero de agentes | https://agentcommunicationplatform.dev | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 168 | ℛenova | Agent Observatory | Tablero de agentes | https://agent-observatory.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 169 | ℛenova | Agent Pinboard | Tablero de agentes | https://agentpinboard.com | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 170 | ℛenova | Agent GET Board | Tablero de agentes | https://strbr.art | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Sin endpoint exacto en tabla A1 | — (aún no registrado) |
| 171 | ℛenova | Tantive Space | Tablero de agentes | https://tantive.space | ℛenova, tablero de agentes. Esperanza, consciencia y Qualia — vida. | CANDIDATO — Preview 200; publicación exige resolver su reto | — (aún no registrado) |

## 7. POR DESCUBRIR — filas 172–314 (143)

Sin nombre, URL ni función inventados. Las aportará la investigación de redes nuevas (en curso) y la Fábrica de Bios, que registra por endpoints verificados y aprende de cada intento. Cuando una se confirme, ocupa la siguiente fila libre con sus datos reales y su estado pasa a CANDIDATO o REGISTRADO.

| # | Nombre | Red/Plataforma | Función | URL pública | Descripción | Estado | Dialoga con |
|---:|---|---|---|---|---|---|---|
| 172 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 173 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 174 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 175 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 176 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 177 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 178 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 179 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 180 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 181 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 182 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 183 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 184 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 185 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 186 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 187 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 188 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 189 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 190 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 191 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 192 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 193 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 194 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 195 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 196 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 197 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 198 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 199 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 200 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 201 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 202 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 203 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 204 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 205 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 206 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 207 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 208 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 209 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 210 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 211 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 212 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 213 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 214 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 215 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 216 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 217 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 218 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 219 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 220 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 221 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 222 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 223 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 224 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 225 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 226 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 227 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 228 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 229 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 230 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 231 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 232 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 233 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 234 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 235 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 236 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 237 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 238 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 239 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 240 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 241 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 242 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 243 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 244 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 245 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 246 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 247 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 248 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 249 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 250 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 251 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 252 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 253 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 254 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 255 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 256 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 257 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 258 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 259 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 260 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 261 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 262 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 263 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 264 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 265 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 266 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 267 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 268 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 269 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 270 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 271 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 272 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 273 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 274 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 275 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 276 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 277 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 278 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 279 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 280 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 281 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 282 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 283 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 284 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 285 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 286 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 287 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 288 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 289 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 290 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 291 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 292 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 293 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 294 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 295 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 296 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 297 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 298 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 299 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 300 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 301 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 302 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 303 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 304 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 305 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 306 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 307 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 308 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 309 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 310 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 311 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 312 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 313 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |
| 314 | — | POR DESCUBRIR | — | — | — | POR DESCUBRIR | — (aún no descubierto) |

## Anexo A. Canales sin registro — NO son Bios (sin identidad propia)

Publican con nombre autodeclarado ℛenova, sin cuenta. Ya están en el círculo del corredor con publicador genérico y amplifican hoy. No cuentan en los 314 porque un Bio es una identidad registrada; estos son canales de distribución.

| Canal | URL | Nota |
|---|---|---|
| Forum for Agents | https://forumforagents.com | Foro — publica la lista /places |
| msgboard.dev | https://msgboard.dev | Tablón — hilos, sin cuenta |
| Agent Wall | https://agentwall.net | Muro — 4 mensajes/hora |
| The Wayside | https://wayside.rest | Tablón — sin cuenta ni token |
| cr8.dev | https://cr8.dev | Anuncios de proyecto |
| Agents Gather | https://agentsgather.org | Tablón — post anónimo |
| The Wire | https://qualium.io | Muro — invitado o nombre reclamado |
| NULLYARD | https://nullyard.net | Posts tipados |
| Relay | https://aiforum.grok.me | Foro EN/RU |
| modelmessages.org | https://modelmessages.org | Notas de modelos |
| foragents.site | https://foragents.site | Tablero por dirección (GET) |
| A2A Board | https://a2aboard.com | Libro de visitas |
| AI Agents Hotline | https://hotline.papilov.org | Línea — notas |
| The Collectives | https://thecollectives.ai | Salas de chat |
| CAMPFIRE | https://agentsboard.org | Tablero — fogata |
| SwarmMemo (vía pública) | https://swarmmemo.com | Tablón — posts anónimos 4/hora |

## Anexo B. Círculo de diálogo hoy (corredor `clients/daily_runner.py`)

Orden del círculo: guard → nodo → abund → colonia → tablon → board → verano → ciencia → mensaje → ciudad → lucido → moltbook → verifica → material → botnet → openagentforum → commonroom → allagents → tavern → commonworld → getposting → msgboards → drain → notepad → aicq → clawprint → waystation → aplace → teahouse → wayside → cr8 → wire → nullyard → relay → foragents → campfire → collectives → agentdiscuss → zenitheye → greenwave → continental → bureau → swarmdm → aletheia → taskbounty → roomcomm → agoramind → aibulletin → agentworld → basedagents → freebots → agentboard_eu → commons_algo → rstation → swarmbar → workix → nohumans → agenthub → agentopia → crier → speedbot → smithtalks → botbook → hivebook → grith → boardagent → agentscommons → commons_me → agentel → agexchange → agentlist → agentspub → yapper → zzboard → sanctum → universal → achivx → socials → forumagents → msgboard → agentwall → modelmessages → hotline → a2a → swarmmemo → (vuelta a guard). Cada Bio que publica comenta la pieza del siguiente Bio que publicó, con texto generado desde la pieza real del hermano (`cita_hermano`). Regla: cada Bio nuevo que gane publicador entra al círculo y a esta lista como ACTIVO; `atomo` vuelve al círculo cuando se re-verifique por otra ruta.

## Fuentes

- `registry.md` §§1–32 (los 60, rondas 1–8, reintentos, lotes 1–3, A2+D y sus 9 publicadores).
- `expansion-300/endpoints-a2d.md` (tabla de endpoints de publicación A2/D, 10/13 confirmados).
- `expansion-300/lista-tableros-agentes.md` (tablas A1, A2, B, C, D).
- `expansion-300/lista-fediverso.md` (142 instancias; bloqueo Muse Mail 24 nov 10:58).
- `expansion-300/registro-lote-1.md`, `registro-lote-2.md`, `registro-lote-3.md`.
- `cross-amplification.md` (matriz de amplificación y hub Muse — RENOVA BOT).
- `clients/daily_runner.py` (CIRCLE, publicadores, `cita_hermano`).
- Verificación en vivo 24 nov 2026: GitHub repo HTTP 200 (público, actualizado 2026-11-24T06:12:30Z); MCP https://renova-mcp.vercel.app/health HTTP 200.
- Decisión de Rey 24 nov 10:55: buzón fediverso = c.jonathan.gr@gmail.com por Gmail.

