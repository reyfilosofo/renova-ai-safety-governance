# RENOVA AI SAFETY & GOVERNANCE

Programa experimental de investigación e ingeniería de **Rey Filósofo / SERESARTE / ℛenova** sobre agencia de IA segura, reversible y con supervisión humana.

> **Estado: prototipo de laboratorio.** Este repositorio recoge el contenido del programa tal como quedó en el espacio unificado RENOVA AI SAFETY & GOVERNANCE, construido el 17 de noviembre de 2026. No certifica sistemas, no afirma mitigación de riesgos de AGI o de superinteligencia y no sustituye a la investigación de alineamiento.

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
- **Sin licencia: el proyecto sigue UNLICENSED.** No hay archivo de licencia en este repositorio a propósito.

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
| `CENTRO-001-preregistro.md` | Preregistro del experimento CENTRO-001 |
| `benchmark/` | Benchmark ℛ v0.1: diseño y lote inicial R-001–R-040 |
| `packages/PACKAGES.md` | Inventario de los paquetes del producto (los archivos .zip no están incluidos; ver esa nota) |

## Procedencia de los archivos

- Los tres documentos fundacionales (`docs/01`, `02`, `03`) y el diseño del Benchmark ℛ son **verbatim** de los documentos entregados por el autor.
- Las secciones del programa (`dictamen`, `centro-001`, `simulador`, `laboratorio`, `estándares`, `ruta dual`, `valor`, `bitácora`) son transcripciones fieles del registro verificado del programa. El código fuente del espacio no se leyó directamente para elaborarlas.
- `centro-guard-policy.yaml` y `CENTRO-001-preregistro.md` son reconstrucciones fieles a partir del registro verificado del programa: las versiones generadas en el navegador por la página v3.33 (retirada) no están disponibles como texto.
- Los paquetes `.zip` y el `.docx` del Governance Test **no están incluidos** en este repositorio: el conector de GitHub no admite contenido binario. `packages/PACKAGES.md` los inventaría con nombre, fecha, número de archivos, md5 y resultados verificados, para subirlos por la web de GitHub, por git o como Releases.

## Ecosistema

Sitios hermanos del mismo programa. No hay conexión técnica en vivo entre ellos.

- **Laboratorio público (ChatGPT)** — Public Research Lab 1.1.0: https://renova-safety-governance.seresarte.chatgpt.site
- **Consola R1 (Grok)** — RENOVA AI Safety: https://aisafety.grok.me
- **Espacio en Muse** — RENOVA AI SAFETY & GOVERNANCE: https://muse.ai/s/renova-ai-safety-governance-mu6xbxa4f1vxrm/lNYv7EadoL3SpqDu-8T_D2UuyOGXr8Y7WZcLh80sxjQ
- **Repo del agente** — https://github.com/reyfilosofo/renova-agent
