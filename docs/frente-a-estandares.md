# Frente a los estándares — interoperar, no competir

Todo lo de esta sección es **OBJETIVO DE INTEROPERABILIDAD**, no compatibilidad verificada, afiliación, respaldo ni certificación. **Ninguna de estas instituciones ha respaldado RENOVA.**

## OWASP Agent Control Standard (ACS)

Un componente Guardian independiente puede permitir, denegar o modificar operaciones de un agente por un canal autenticado y con trazabilidad, con perfiles de observabilidad y evidencia criptográfica. Decisión RENOVA: no construir desde cero otro estándar general de autorización para competir con ACS; examinar su interoperabilidad con CENTRO y aportar solo lo adicional — políticas explícitas de reversibilidad, consecuencias humanas, daño no desplazado y revisión de legitimidad (RNV-01 a RNV-06) — con pruebas de si esos criterios mejoran las decisiones frente a políticas existentes.

## NIST AI RMF y NIST AI 600-1

Referencia de gestión de riesgos, confianza, evaluación y responsabilidades (AI RMF 1.0, enero de 2023: GOVERN / MAP / MEASURE / MANAGE; AI 600-1, julio de 2024: perfil GenAI con 12 riesgos y más de 200 acciones). RENOVA aporta como objetivo una matriz de evidencia (qué se afirma, con qué evidencia, en qué estado), no una adecuación ni certificación. Ver también `ruta-dual-nist-renova.md`.

## Inspect AI (UK AI Security Institute)

Infraestructura abierta con más de 200 evaluaciones predefinidas, datasets, herramientas, agentes y sandboxes. RENOVA no crea otro evaluador general; su aporte como objetivo es un adaptador de pruebas — comprobar integridad de permisos y decisiones antes de ejecutar, y conservar evidencia verificable para revisión humana.

## METR

Propuesta sobre evaluar mecanismos de control y supervisión de agentes internos (14 de octubre de 2026). Cinco problemas: cobertura de la supervisión, vulnerabilidades del monitor, evasión, respuesta humana y medición. RENOVA lo toma como referencia de evaluación, no como validación.

## IMDA Singapur

Gobernanza para IA agéntica. Referencia de contexto para el gobierno de agentes; su inclusión no implica asociación ni respaldo.

## Lo que sigue

(a) Congelar la expansión horizontal y concentrarse en CENTRO Guard. (b) Ejecutar CENTRO-001 con preregistro. (c) Completar la revisión ciega del Benchmark ℛ con Revisor A, Revisor B y adjudicador independientes. (d) Corregir el bug de WarRoom (`random.exponential`) y la fórmula RATIO garabateada en la consola EGRA de Grok. (e) Decidir sobre un ZK-Prover real o retirar «zk-SNARK» y `VERIFIED_COMPLIANT`. (f) Decisión de revisión/merge del PR #52 con sus controles pendientes. (g) Añadir el bloque Ecosistema dentro de ChatGPT y Grok (ya está en Muse). (h) Prueba federada preregistrada R2 solo después de CENTRO-001.
