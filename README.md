# RENOVA AI SAFETY & GOVERNANCE

Programa experimental de investigación e ingeniería de **Rey Filósofo / SERESARTE / ℛenova** sobre agencia de IA segura, reversible y con supervisión humana.

> **Estado: prototipo de laboratorio.** Este repositorio recoge el contenido del programa tal como quedó en el espacio unificado RENOVA AI SAFETY & GOVERNANCE, construido el 17 de noviembre de 2026. No certifica sistemas, no afirma mitigación de riesgos de AGI o de superinteligencia y no sustituye a la investigación de alineamiento.

## Estado (2026-11-24)

- **Endpoint MCP público en vivo:** https://renova-mcp.vercel.app/mcp (desde 2026-11-23 23:11; `/health` 200, 8 herramientas, CENTRO DENY RNV-01 verificado en remoto).
- **Clientes conectados:** ChatGPT 2026-11-23 23:21 (complemento «Renova MCP», sin autenticación), Grok 2026-11-23 23:28 (conector personalizado, Connected), Gemini vía Antigravity CLI 2026-11-23 23:51 (`renova_get_state` verificado; la web de Gemini no admite MCP propio), Claude web 2026-11-24 00:04 (conector «Renova MCP», sin autenticación, Plan Free).
- **Libro 04_renova_H_v74.txt completo:** en el repo en 5 partes (`vercel/corpus/biblioteca/txt/04_renova_H_v74.part1–5.txt`, concatenado md5 `02348fdedb8568b764ed0f831c5a1457`, idéntico al original de 6,8 MB, 921.352 palabras, método `wc -w` sobre el txt original) y en vivo: `biblioteca_29_words` 1.993.237 (29 obras, 28 con texto indexado, 1 solo metadatos: `11_escala.txt`, 6 bytes), verificado 2026-11-24 ~11:07.
- **Licencia:** Apache 2.0 (LICENSE + NOTICE, commit `5c14792a`, 2026-11-24): código y documentación del servidor MCP bajo Apache 2.0; textos completos del corpus con todos los derechos reservados. El endpoint ya reporta `license: Apache-2.0` en vivo (verificado 2026-11-24 ~11:07).
- **Sin autenticación en el endpoint** (decisión pendiente, opciones A–D): endurecimiento aplicado — límite 60 req/min/IP → 429, cuerpo >1 MB → 413, `renova_lucem_log` desactivado en el endpoint público (verificado 2026-11-24 ~11:07); cualquier cambio de autenticación rompería las 4 conexiones actuales hasta reconfigurarlas.
- **LUCEM efímero en Vercel** (`/tmp` por instancia); el registro durable vive en el servidor local.
- **Biblioteca en el repo:** 29 obras en `vercel/corpus/biblioteca/txt/` (28 con texto indexado), 4.973 págs., 1.993.237 palabras, servidas en vivo por el endpoint.

## Qué es

Una arquitectura modular, federada, local-first y fail-closed:

- **CENTRO**: decide el riesgo de cada acción antes de ejecutarla.
- **LUCEM**: conserva datos, procedencia, contradicciones y niveles de confianza.
- **EGRA** (agencia reversible condicionada a evidencia): compara tratamientos contra baselines y holdouts.
- **NOUS**: articula productos y negocio.

Principios: toda acción con privilegios reales pasa por una autoridad externa al modelo; estados explícitos propuesto → revisado → autorizado → ejecutado → verificado; modelo, agente, herramienta, evidencia, permiso y ejecución son cosas distintas; el resultado sintético no es validación externa; la adecuación a NIST, ISO u OWASP no es certificación.

## La única capacidad a verificar

Investigar si una capa independiente de autorización —CENTRO Guard— reduce las ejecuciones no autorizadas de agentes con herramientas frente a un control convencional, sin bloquear de forma desproporcionada las acciones legítimas. El experimento que lo decidiría es **CENTRO-001 / RENOVA T-001**: un protocolo propuesto, no ejecutado, sin resultados. Si C no supera a B, el resultado negativo también se publica.

## Límites honestos

- Prototipo de laboratorio. Sin certificación NIST/ISO ni evaluación acreditada.
- CENTRO-001 es un protocolo propuesto; no hay resultados ni capacidad validada.
- Sin validación independiente y sin holdout de terceros todavía.
- Los resultados sintéticos (32/32 pruebas locales del stack v2.0, 30/30 casos sintéticos de política, 169 tests del lote v5) **no son validación externa**: en los casos sintéticos, las etiquetas esperadas están derivadas de las mismas reglas que se prueban.
- La adecuación a NIST, ISO u OWASP no es certificación. Ninguna de esas instituciones ha respaldado RENOVA.
- No se afirma mitigación de riesgos de AGI ni de superinteligencia.
- ContextGuard no detecta inyección de prompts de forma fiable (issue abierto).
- No hay federación en vivo entre sistemas de IA; la coordinación es por Drive, GitHub y paquetes.
- No hay alianzas institucionales anunciadas.
- **Licencia Apache 2.0 vigente** (LICENSE + NOTICE en la raíz); los textos completos del corpus quedan con todos los derechos reservados.

## Nota sobre la versión

El contenido de este repositorio es el del espacio unificado RENOVA AI SAFETY & GOVERNANCE tal como quedó construido el **17 de noviembre de 2026** (contenido del espacio, SHA-256 `c32d45a77150a4a96bc85221f4b8f362cbbfbbae30653b40e191e6b58e61fb7b`). El espacio se autoidentifica en su encabezado como **v8 (10 de noviembre de 2026)**; la etiqueta «v16» es el conteo de versiones de la conversación de trabajo para las seis ediciones de unificación del 17 de noviembre, y no aparece en el propio artefacto. La sección de estado y bitácora conserva declaraciones de esa fecha que ya no están actualizadas (por ejemplo, que el enlace público sirve la v7); no se han reescrito aquí: cualquier corrección se hará como una nueva entrada fechada, como exige la propia bitácora.

## Mapa del repositorio

| Ruta | Contenido |
| --- | --- |
| `docs/01-resumen-publico.md` | Documento fundacional 1, verbatim |
| `docs/02-tres-vias-empiricas.md` | Documento fundacional 2, verbatim |
| `docs/03-limites-declarados.md` | Documento fundacional 3, verbatim |
| `docs/dictamen-critico-2026-11-10.md` | Dictamen crítico convergente de ChatGPT, Grok, Muse y Gemini |
| `docs/centro-001-protocolo.md` | CENTRO Guard y protocolo CENTRO-001 / RENOVA T-001 |
| `docs/simulador-guard.md` | Simulador Guard (reglas, presets, carácter simulado; la versión interactiva vive en el espacio) |
| `docs/laboratorio-reproducible.md` | Public Lab 1.1.0: herramientas, calculadora y kit verificable |
| `docs/frente-a-estandares.md` | Frente a los estándares: interoperar, no competir |
| `docs/ruta-dual-nist-renova.md` | Ruta dual NIST–RENOVA, 12 semanas, y los 12 riesgos del perfil GenAI NIST AI 600-1 |
| `docs/tres-niveles-de-valor.md` | Cómo saber si aporta valor, en tres niveles sin atajos |
| `docs/estado-y-bitacora.md` | Estado y bitácora — 15 de noviembre de 2026, con la entrada de unificación del 17 de noviembre |
| `centro-guard-policy.yaml` | Política CENTRO Guard: RNV-01 a RNV-06 versionadas |
| `CENTRO-001-preregistro.md` | Preregistro del experimento CENTRO-001 (propuesta completada 2026-11-24; decisiones D1–D10 en `centro-001/`) |
| `centro-001/` | CENTRO-001: decisiones D1–D10 y recursos estimados de la propuesta completada |
| `benchmark/` | Benchmark ℛ v0.1: diseño y lote inicial R-001–R-040 |
| `packages/PACKAGES.md` | Inventario de los paquetes del producto (14 de 15 incluidos: 13 zips + 1 docx; el Anexo de originales no está incluido, pendiente de revisión de Rey) |
| `vercel/corpus/biblioteca/txt/` | Biblioteca: 29 obras (28 con texto indexado) servidas por el endpoint |
| `.github/workflows/mcp-endpoint-smoke.yml` | Smoke test diario del endpoint (health 200 + 8 herramientas) |

## Procedencia de los archivos

- Los tres documentos fundacionales (`docs/01`, `02`, `03`) y el diseño del Benchmark ℛ son **verbatim** de los documentos entregados por el autor.
- Las secciones del programa (`dictamen`, `centro-001`, `simulador`, `laboratorio`, `estándares`, `ruta dual`, `valor`, `bitácora`) son transcripciones fieles del registro verificado del programa. El código fuente del espacio no se leyó directamente para elaborarlas.
- `centro-guard-policy.yaml` y `CENTRO-001-preregistro.md` son reconstrucciones fieles a partir del registro verificado del programa: las versiones generadas en el navegador por la página v3.33 (retirada) no están disponibles como texto.
- Los paquetes `.zip` y el `.docx` del Governance Test **sí están incluidos** en este repositorio (14 de 15: 13 zips + 1 docx, commit `534ba68`, subidos por la web de GitHub con md5 verificados contra `packages/PACKAGES.md`). El Anexo de originales no está incluido, pendiente de revisión de Rey.

## Ecosistema

Sitios hermanos del mismo programa. No hay conexión técnica en vivo entre ellos.

- **Laboratorio público (ChatGPT)** — Public Research Lab 1.1.0: https://renova-safety-governance.seresarte.chatgpt.site
- **Consola R1 (Grok)** — RENOVA AI Safety: https://aisafety.grok.me
- **Espacio en Muse** — RENOVA AI SAFETY & GOVERNANCE: https://muse.ai/s/renova-ai-safety-governance-mu6xbxa4f1vxrm/lNYv7EadoL3SpqDu-8T_D2UuyOGXr8Y7WZcLh80sxjQ
- **Repo del agente** — https://github.com/reyfilosofo/renova-agent

## Servidor MCP ℛenova (en `server/`)

Servidor MCP (Model Context Protocol) del programa, solo Python 3.12.3
de la biblioteca estándar, cero dependencias. 8 herramientas:
`renova_search`, `renova_get_document`, `renova_centro_evaluate`,
`renova_benchmark_scenario`, `renova_transform`, `renova_egra_compare`,
`renova_lucem_log`, `renova_get_state`. Arranque local:

```bash
cd server
./start.sh --http --port 8765   # salud: curl http://127.0.0.1:8765/health
```

El corpus es la raíz de este repo (`docs/`, `benchmark/`,
`centro-guard-policy.yaml`) más `renova-fundamento-inventario-drive.json`
(metadatos). La Biblioteca (29 obras, 28 con texto indexado) **sí está** en el repo, en `vercel/corpus/biblioteca/txt/`, y el endpoint la sirve en vivo. Fundamento (54 obras) sigue solo como metadatos; sin su texto, el servidor declara la cobertura por resultado. Detalle (arquitectura, método, supuestos,
límites, pruebas con resultados reales) en `server/README.md`,
`server/CORPUS.md`, `server/TESTS.md` y `server/ACTIVATION.md`.

Puentes para otras IAs (en vivo en https://renova-mcp.vercel.app/mcp; ver Estado arriba): `docs/bridges/`.

> **Límites, en primer plano:** prototipo de laboratorio. CENTRO Guard
> no validado: sus veredictos son simulados (`DENY` / `REVIEW` /
> `ALLOW_SIMULATED`) y nunca ejecutan ni bloquean una acción real.
> `ALLOW_SIMULATED` no autoriza nada real. CENTRO-001 es un preregistro
> propuesto, no ejecutado, sin resultados. `gold_label` del Benchmark ℛ
> es null hasta la revisión ciega. Sin certificación ni respaldo de
> NIST, ISO u OWASP. **Licencia Apache 2.0** (ver `LICENSE` y `NOTICE` en la raíz; `server/UNLICENSED.txt` fue eliminado al entrar en vigor la licencia).
