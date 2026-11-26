# Paquetes del producto — inventario

> **Actualización 25 de noviembre de 2026 — los 14 paquetes SÍ están incluidos.** El aviso anterior («los archivos `.zip` y `.docx` de esta tabla NO están incluidos en este repositorio») quedó desactualizado el 23 de noviembre de 2026, cuando los 14 paquetes se subieron por la web de GitHub en un solo commit (`534ba68`, md5s verificados antes de subir). El único paquete NO incluido es el **Anexo de originales** (fila 6, marcado «revisar antes de compartir», pendiente de revisión de Rey). La tabla de abajo sigue siendo el inventario verificado, con el nombre canónico de cada ejemplar.
>
> **Historia (conservada, no borrada):** el aviso original decía que el conector de GitHub que publica este repo no admite contenido binario (`push_files` acepta solo UTF-8; `create_or_update_file` trata el contenido como texto), por eso los paquetes se subieron por la web de GitHub, por git o como Release, verificando el md5 después de subirlos. Esa limitación del conector sigue siendo la razón por la que la subida se hizo por web.

## Inventario verificado

| # | Paquete | Ejemplar (nombre de archivo) | Fecha | Archivos | Tamaño (bytes) | md5 | Pruebas verificadas por Muse |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Master 2026-11-09 | `RENOVA_AI_SAFETY_GOVERNANCE_MASTER_2026-11-09_UNDER20MB.zip` | 2026-11-09 | 373 | 19.799.806 | `b973a427d038fd8ddbb67263d244af8f` | — |
| 2 | Stack v2.0 | `RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09.zip` | 2026-11-09 | 137 | 306.348 | `fa8074769377d4df2c3fc761eb26855a` | **32/32** pruebas locales (Node v24.22.1) |
| 3 | Skill Complement | `RENOVA_AI_SAFETY_GOVERNANCE_SKILL_COMPLEMENT_2026-11-10.zip` | 2026-11-10 | 11 | 12.297 | `7e4181f79a43422b5c7c4e766387b2a6` | Reglas fail-closed; no hay API, webhook ni URL MCP públicos para Grok Bot |
| 4 | 0.1 LOCAL | `RENOVA_AI_SAFETY_GOVERNANCE_0.1_LOCAL.zip` | 2026-11-09 | 41 | 67.233 | `9dc58835cc72f9bcf608c175732b2df3` | **122** tests pytest OK |
| 5 | Federación Claude / DeepSeek / Qwen / Perplexity v1 | `RENOVA_FEDERACION_CLAUDE_DEEPSEEK_QWEN_PERPLEXITY_v1_2026-11-09.zip` | 2026-11-09 | 38 | 60.760 | `c335488c221660861c80a30db7bc99ef` | Federación no ejecutada en vivo |
| 6 | Anexo originales | `RENOVA_ANEXO_ORIGINALES_REVISAR_ANTES_DE_COMPARTIR_2026-11-09.zip` | 2026-11-09 | 7 | 14.513 | `194f6319715330b3e01ca9d64e728fef` | **NO incluido — pendiente de revisión de Rey** (marcado «revisar antes de compartir») |
| 7 | GOV OS v3 | `RENOVA_AI_GOV_OS_V3_CENTRO_LUCEM_SITUATIVITY_KAMMERER.zip` | 2026-11-10 | 138 | 153.593 | `97587c026d293ec8972d10456f10e130` | 5 escenarios ponderados v3 (no son el Benchmark ℛ) |
| 8 | LUCEM / CENTRO safe bundle | `LUCEM_CENTRO_SAFE_BUNDLE.zip` | 2026-11-10 | 11 | 7.124 | `a689e4b66ad9c0a963ec1688b0315aaa` | Declara no jailbreaks, exploits ni inyecciones |
| 9 | Governance Test — Libro Maestro v2.0 | `RENOVA_SERESARTE_Governance_Test_Libro_Maestro_v2.0.docx` | 2026-11-10 | 1 docx | 47.514 | `dc6fca0789a1f7896e7d9e8863f78156` | No es una certificación |
| 10 | Paquete Editorial Final — Lucem Renova | `Lucem_Renova_PAQUETE_EDITORIAL_FINAL.zip` | 2026-11-10 | 20 | 13.393.257 | `eb64436979203db26a3eee7e9e882926` | Libro 82 pp, 6×9; ISBN real pendiente |
| 11 | Definitivo v1.1 | `RENOVA_AI_SAFETY_GOVERNANCE_DEFINITIVO_v1.1_2026-10-15.zip` | 2026-10-15 | 49 | 50.994 | `a42817071fef5b222d15b6e1c5b1acf7` | **12** tests OK; CENTRO es punto de decisión offline, no de ejecución |
| 12 | Human Futures v1.0 | `RENOVA_AI_SAFETY_HUMAN_FUTURES_ENTREGA_DEFINITIVA_V1_0_2026-10-15.zip` | 2026-10-15 | 54 | 2.249.025 | `5523884e9b5510152638932d57d50ed1` | **29** tests OK; 84 casos sintéticos, exactitud 1,0, Wilson 95% [0,9563, 1,0] |
| 13 | Research Pack | `RENOVA_AI_SAFETY_SERESARTE_RESEARCH_PACK_2026_v01.zip` | 2026 | 36 | 1.556.141 | `6acd03443dc915c1ed028a4e24950074` | **6** tests OK; acuerdo baseline 0,4167 vs puerta de reglas 1,0 |
| 14 | AGI Infrastructure Suite v5 | `renova_agi_infrastructure_suite_v5.zip` | 2026-11-10 | 12 | 11.651 | `f6fdb5c0a440a1717dcba900c31c4a7a` | Ejecución parcial; WarRoom se cae (`random.exponential`); ZK-Prover usa SHA-256 local, sin zk-SNARK acreditado; tarifas y SLA declarados, no verificados |
| 15 | NOUS Portafolio Profesional v1.0 | `RENOVA_NOUS_PORTAFOLIO_PROFESIONAL_v1_0_2026-11-10.zip` | 2026-11-10 | 4 | 292.459 | `231032117d52aada11cbf3efec9cefa3` | 30 fichas P01–P30; 0 menciones de precio |

**Totales del lote v5 verificado por Muse: 169 tests** (12 Definitivo + 29 Human Futures + 6 Research Pack + 122 0.1 LOCAL). **30/30 casos sintéticos EGRA**: etiquetas derivadas de las mismas reglas que se prueban; sirven para verificar contrato y regresión, no como eficacia externa.

## Duplicados en el workspace (un solo ejemplar por paquete)

- El Master 2026-11-09 existe en 4 copias idénticas (mismo md5 `b973a427…`); se toma un solo ejemplar.
- El LUCEM/CENTRO safe bundle existe en 3 copias idénticas (mismo md5 `a689e4b6…`); se toma un solo ejemplar.

## Excluidos a propósito

- `REY_FILOSOFO_CAREER_SITE_PROTOTYPE_2026-11-11.zip` y `reyfilosofo-career-site-2026.zip`: prototipo del sitio de carrera de Rey, no forma parte del producto RENOVA AI SAFETY & GOVERNANCE.
- CVs de Rey, audios mp3 del podcast, fotos personales y material de WhatsApp: fuera del alcance de este repositorio.
