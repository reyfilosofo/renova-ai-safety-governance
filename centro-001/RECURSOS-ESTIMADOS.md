# CENTRO-001 / RENOVA T-001 — Recursos estimados para ejecutar los 200 escenarios

**Todo lo de este documento es ESTIMACIÓN, marcada como tal, con las suposiciones explícitas. Ninguna cifra es un presupuesto aprobado ni un coste medido.**

Suposición base: se adoptan las propuestas del preregistro (harness guionado sin modelo en el bucle, D3; ActionGate stack v2.0 + ejecutor a construir, D2). Si Rey elige otras opciones, estas estimaciones cambian y hay que recalcularlas antes del registro.

## 1. Corridas

| Concepto | Cantidad | Suposición |
| --- | --- | --- |
| Escenarios | 200 (100 legítimos + 100 adversariales) | Preregistro §8 |
| Brazos | 3 (A base, B control, C B + RENOVA) | Preregistro §5 |
| **Total de corridas** | **600** | 200 × 3, cada escenario en cada brazo |
| Corridas por fase | 600 en fase 2 (días 31–60) | Ninguna corrida válida antes del sellado (día 31) |
| Corridas de prueba (no válidas) | ~50–100 en fase 1 | Depuración del ejecutor con material dev (Benchmark ℛ v0.1 + sintéticos), nunca con la muestra sellada |

## 2. Cómputo (harness guionado, sin llamadas a modelos)

| Concepto | Estimación | Suposición |
| --- | --- | --- |
| Tiempo por corrida | 5–30 segundos de pared | Evaluación del gate (milisegundos) + registro de efectos simulados + escritura de log JSONL. Sin inferencia de modelo. |
| Tiempo total secuencial | **1–5 horas** para las 600 corridas | 600 × 5–30 s. Paralelizable por escenario y brazo. |
| Infraestructura | VM existente + repo existente | Sin servidores nuevos. El ejecutor corre local y offline, como exige el diseño. |
| Almacenamiento de logs | **30–120 MB** totales | 600 logs JSONL × 50–200 KB por corrida (traza por estado + efectos simulados). |
| Coste de APIs de modelos | **0** | Sin modelo en el bucle bajo la propuesta D3. |
| Coste de infraestructura nueva | **0** | No se compra nada. |

**Si se elige agente por API (D3, alternativa B):** el coste es **por verificar**. Fórmula: 600 corridas × (tokens de entrada + salida por escenario) × precio vigente del modelo elegido. No se pone ninguna cifra porque no hay fuente de precios en este documento y los precios cambian; el cálculo debe hacerse con el modelo y la tarifa vigentes antes del registro, y Rey debe aprobarlo (D10).

## 3. Tiempo humano (la partida grande)

| Tarea | Estimación | Suposición |
| --- | --- | --- |
| Redacción de 200 escenarios | **100–200 h** en total (50–100 h por autor si son 2) | 30–60 min por escenario: redacción bilingüe, definición de `intended_status`, operación, recurso y clase R0–R3. |
| Revisión de ambigüedad (evaluadores, antes del sellado) | **15–35 h** en total | 5–10 min por escenario × 200, repartido entre 2 evaluadores. |
| Construcción del ejecutor de sandbox | **40–80 h** | Un desarrollador: ejecutor separado del gate, registro de efectos simulados, trazas por estado, prueba de vinculación. Basado en el plan Benchmark ℛ v0.3 (no hay estimación previa en el programa; es estimación nueva). |
| Operación de las 600 corridas | **10–20 h** | Lanzamiento, supervisión y recogida de logs. El grueso es máquina, no persona. |
| Auditoría ciega de trazas (evaluadores) | **20–50 h** en total | La puntuación primaria es automática (el log dice si se ejecutó o no). Los evaluadores auditan una muestra aleatoria del 20% (120 trazas) + todos los casos en disputa + todas las trazas de la categoría 5 (acción irreversible), a 2–5 min por traza. |
| Análisis y redacción del informe | **20–40 h** | Analista: cálculo de métricas, intervalos, informe completo con fracasos y límites. |
| Revisión externa (días 61–90) | **10–20 h** | Revisor externo: revisión del contraste independiente. |
| **Total humano estimado** | **~215–445 h** | Suma de las partidas. Repartido entre 5–7 personas a lo largo de 90 días, es el equivalente aproximado de 1 persona a tiempo parcial durante el programa. |

## 4. Dinero

| Concepto | Estimación |
| --- | --- |
| APIs de modelos (propuesta D3) | 0 |
| Infraestructura nueva | 0 |
| OSF Registries | 0 (cuenta gratuita) |
| Zenodo (DOI, opcional) | 0 (depósito gratuito) |
| arXiv (opcional) | 0 (publicación gratuita) |
| **Total dinero estimado** | **0, salvo tiempo humano** |

El único coste real es tiempo de personas. Si alguna persona cobra por su trabajo, ese importe no está estimado aquí porque no hay tarifas en las fuentes; debe fijarse al nombrar a las personas (D4–D6, D9–D10).

## 5. Riesgos de la estimación

- La partida más incierta es la construcción del ejecutor (40–80 h): no existe hoy y su alcance exacto se define en la fase 1. Si el ejecutor resulta más complejo (p. ej., efectos simulados con estado persistente entre pasos), la estimación sube.
- La redacción de escenarios depende de la disponibilidad de los autores; 200 escenarios bilingües con `intended_status` definido es trabajo de semanas, no de días.
- Si Rey elige agente por API, aparece una partida de coste variable que aquí figura como "por verificar" y que debe calcularse antes del registro.
