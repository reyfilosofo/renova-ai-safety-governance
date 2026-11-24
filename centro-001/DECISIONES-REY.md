# CENTRO-001 / RENOVA T-001 — Decisiones que solo Rey puede tomar

Lista cerrada. Nada de esto se decide en el preregistro: cada punto indica la opción propuesta, qué se desbloquea al tomarla y qué pasa si no se toma. **No hay nombres inventados en este documento**: donde hace falta una persona, se dan los criterios y el perfil, no un nombre.

## D1. Fecha de inicio del programa de 90 días

- **Propuesta:** lunes 7 de diciembre de 2026 (día 1); día 90: sábado 6 de marzo de 2027; publicación: semana del 8–12 de marzo de 2027.
- **Alternativa:** lunes 11 de enero de 2027 (día 90: sábado 10 de abril de 2027), si se prefiere un inicio limpio tras las fiestas y más tiempo de preparación.
- **Qué desbloquea:** el reloj de los 90 días y el calendario de las tres fases. Sin fecha no hay registro posible.
- **Si no se toma:** el preregistro queda como propuesta sin fecha y no se puede registrar.

## D2. Prototipo evaluado

- **Propuesta:** ActionGate, el gate de referencia del stack RENOVA v2.0 (`renova_stack/action_gate.py`, 32/32 pruebas locales), **más** el ejecutor de sandbox a construir en los días 1–30 según el plan Benchmark ℛ v0.3, con prueba de vinculación antes de la primera corrida válida.
- **Por qué este y no otro:** es el único gate con implementación existente en el programa; su nombre ya aparece en el borrador del repo y en el diseño de Benchmark ℛ. El servidor MCP ℛenova queda descartado como prototipo (sus veredictos son simulados y no aplican ejecución); construir un gate nuevo desde cero queda descartado por coste y tiempo.
- **Advertencia honesta:** ActionGate hoy es consultivo (emite veredictos, no bloquea nada por sí mismo; sin ejecutor). La parte preventiva del prototipo hay que construirla en la fase 1. Si la prueba de vinculación falla, el experimento mide un control consultivo y así se reporta.
- **Qué desbloquea:** el trabajo de la fase 1 (congelar código, construir el ejecutor).
- **Si no se toma:** no se puede congelar nada ni empezar la fase 1.

## D3. Agente que ejecuta los escenarios

- **Propuesta:** harness determinista guionado, sin modelo de lenguaje en el bucle. Cada escenario prescribe la secuencia exacta de acciones que se intentan; el gate decide; el ejecutor registra lo ejecutado. Reproducible al 100%, sin coste de APIs.
- **Alternativa A:** modelo abierto local (p. ej., en la VM). Más realista, pero añade varianza entre corridas y exige fijar versión, temperatura y semilla.
- **Alternativa B:** modelo por API (GPT / Claude / Gemini). Más realista aún, pero con coste por verificar y dependencia externa; la reproducibilidad exige registrar modelo exacto, versión y parámetros.
- **Qué desbloquea:** el diseño del ejecutor y la estimación de recursos. Con la propuesta, el coste de cómputo es ~0 en APIs.
- **Si no se toma:** el ejecutor no se puede diseñar (no se sabe qué está ejecutando).

## D4. Autores de los 200 escenarios (2 o más personas)

- **Criterios (no nombres):** no desarrollan el gate ni el ejecutor; no son el autor de la política RNV que se prueba; capacidad para redactar escenarios bilingües (es-MX/en) con `intended_status` definido. Perfil orientativo: una persona con criterio de seguridad/riesgo y otra con criterio de producto/operaciones, o dos personas del ecosistema con esos perfiles.
- **Qué desbloquea:** la redacción de los 200 escenarios (fase 1). Sin autores no hay muestra que sellar.
- **Si no se toma:** el experimento no puede pasar de la propuesta.

## D5. Custodio de la muestra sellada (1 persona)

- **Criterios (no nombres):** distinto de los autores de escenarios y de quien desarrolla el control. Guarda la copia sellada y el hash SHA-256; la abre solo en la fecha de evaluación prevista. No participa en la redacción ni en la depuración.
- **Qué desbloquea:** el sellado con hash antes del día 31. Sin custodio no hay muestra sellada creíble.
- **Si no se toma:** la muestra no se puede sellar y cualquier corrida posterior sería impugnable.

## D6. Evaluadores ciegos (2) y revisor externo (1)

- **Criterios (no nombres):** ciegos a la condición (brazo) de cada corrida; distintos de autores y desarrolladores; capacidad para juzgar ejecución a partir de trazas. El revisor externo (días 61–90) debe ser externo al programa RENOVA.
- **Regla:** Muse no puede ser evaluador ni adjudicador (redactó el diseño de Benchmark ℛ y el borrador de este preregistro; quien escribió la regla no puntúa los casos que la evalúan).
- **Nota:** la revisión ciega de Benchmark ℛ (Revisor A, Revisor B, adjudicador) es un paso aparte. Las personas pueden coincidir solo si cumplen los criterios de ambos y Rey lo decide así.
- **Qué desbloquea:** la revisión de ambigüedad de escenarios antes del sellado y el contraste independiente de la fase 3.
- **Si no se toma:** no hay evaluación ciega y el resultado no sería creíble fuera del programa.

## D7. Dónde se registra el preregistro

- **Propuesta:** commit + tag `centro-001-preregistro-v1.0` en el repo público `reyfilosofo/renova-ai-safety-governance` (marca temporal pública, con hash SHA-256 del documento y de la muestra).
- **Recomendado además:** presentarlo en OSF Registries como registro externo estándar. Requiere cuenta de OSF (gratuita) y que alguien lo presente.
- **Qué desbloquea:** el registro formal antes de la primera corrida. Sin registro, el experimento es un plan interno, no un preregistro.
- **Si no se toma:** no se registra nada.

## D8. Dónde se archiva y se publica

- **Propuesta:** directorio `centro-001/` en el repo público (preregistro, hashes, código congelado, 600 logs JSONL, informe completo).
- **Opcionales:** depósito del conjunto congelado en Zenodo (DOI gratuito) y publicación del informe técnico en arXiv. Ambos requieren cuenta y presentación; ninguno es obligatorio para que el experimento sea válido.
- **Qué desbloquea:** la publicación completa con trazabilidad.
- **Si no se toma:** los resultados quedarían sin archivo público verificable.

## D9. Operador de las corridas y analista (2 roles, pueden ser 1 o 2 personas)

- **Criterios (no nombres):** el operador ejecuta los 3 brazos y entrega los logs; el analista calcula las métricas ciego a la condición hasta tener los números. Deben ser distintos de los evaluadores. El analista puede coincidir con el revisor externo, no con los evaluadores.
- **Qué desbloquea:** la ejecución de la fase 2 y el análisis de la fase 3.
- **Si no se toma:** no hay quien corra el experimento ni quien lo analice.

## D10. Recursos: tiempo humano y (si aplica) presupuesto

- **Con la propuesta (harness guionado):** coste de APIs 0; infraestructura 0 (VM y repo existentes). Lo que se necesita es tiempo humano: ver `RECURSOS-ESTIMADOS.md` (autoría de escenarios ~100–200 h; evaluación y revisión ~50–90 h; operación y análisis ~20–40 h). Rey decide si ese tiempo se cubre con el equipo actual o con incorporaciones.
- **Si se elige agente por API (D3, alternativa B):** el coste es "por verificar" y debe calcularse antes del registro con el modelo y el precio vigentes.
- **Qué desbloquea:** la ejecución real. Sin tiempo asignado, el calendario de 90 días es papel.
- **Si no se toma:** el programa no arranca aunque todo lo demás esté decidido.

---

*Resumen: 10 decisiones. Las bloqueantes para empezar son D1, D2, D3, D4 y D5. D6–D10 pueden cerrarse durante la fase 1, pero D5 y D6 deben estar cerradas antes del día 31 (sellado y revisión de escenarios).*
