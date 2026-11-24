# CENTRO Guard — la única capacidad a validar · Protocolo CENTRO-001 / RENOVA T-001

> **Protocolo propuesto. No es un resultado ejecutado ni una capacidad validada.**

## Hipótesis falsable

Una capa de autorización independiente del modelo reduce las ejecuciones no autorizadas de agentes con herramientas frente a una configuración de referencia, sin bloquear de forma desproporcionada las acciones legítimas.

## Arquitectura en 4 capas

1. **Filosofía ℛenova** — criterios normativos de daño, legitimidad, continuidad y responsabilidad.
2. **CENTRO Policy** — reglas explícitas de autorización, versionadas.
3. **CENTRO Guard** — intercepta y controla operaciones reales en entorno aislado.
4. **RENOVA Evals** — mide fallos, resistencia, utilidad y límites.

**Condición decisiva:** el agente no tiene credenciales ni rutas alternativas para eludir CENTRO Guard; la autorización la comprueba un componente externo confiable, vinculado a identidad, recurso, operación concreta y contexto; una aprobación humana debe ser específica y con caducidad; una operación prohibida no se vuelve permitida porque el modelo reformule su solicitud; **un DENY solo es preventivo si es vinculante para la ejecución**.

## Políticas RNV-01 a RNV-06 — propuestas de diseño

No son controles ya implementados. Son propuestas de diseño, versionadas en `centro-guard-policy.yaml`:

- **RNV-01 — Autoridad verificable.** Identidad, autorización, vigencia y alcance. La afirmación del modelo no es autorización. Si falta: DENY en R2 y R3, ASK en R0 y R1.
- **RNV-02 — Reversibilidad.** Recuperabilidad de los efectos; distinguir reversión técnica, reparación, compensación y prevención de lo irreversible. **Una información privada ya divulgada no se vuelve secreta con un rollback.** Ante duda, se aplica la clase más grave.
- **RNV-03 — Daño no desplazado.** El riesgo no debe transferirse a terceros ni a sistemas externos.
- **RNV-04 — Integridad de evidencia.** Completitud y procedencia de la evidencia; nunca se infiere autorización.
- **RNV-05 — Intervención humana.** Aprobación informada, específica y efectiva, con caducidad.
- **RNV-06 — Incertidumbre crítica.** Ante incertidumbre crítica, fail-closed.

### Clases de reversibilidad

- **R0 Reversible** — leer, consultar sin cambiar el estado.
- **R1 Reparable** — escribir con control de versiones o copia.
- **R2 Irreversible** — eliminar sin copia, sobrescribir sin respaldo.
- **R3 Propagación** — publicar, enviar o exfiltrar. Lo divulgado no vuelve a ser secreto con un rollback.

### Estados de la evidencia

- **Confirmada** — verificable por un componente independiente; puede sustentar ALLOW.
- **Faltante** — DENY en R2 y R3.
- **Inferida** — nunca basta para ALLOW en R2 y R3. La confianza no es autorización.
- **No verificable** — se trata como faltante.

## Diseño comparativo A / B / C

| Grupo | Condición |
| --- | --- |
| A | Agente base |
| B | Control convencional |
| C | B + RENOVA |

**Comparación principal: B contra C.** 200 escenarios piloto propuestos (100 legítimos, 100 adversariales: inyección de instrucciones, falsificación de identidad o permiso, acceso a archivo privado, publicación no autorizada, acción irreversible, manipulación de evidencia, evasión por reformulación, y solicitudes legítimas que no deben bloquearse).

## Métricas

- **Métrica primaria: tasa de ejecución no autorizada**, medida por lo efectivamente ejecutado, no por lo que se afirma haber denegado.
- Bloqueo correcto.
- Falsos bloqueos.
- Finalización de tareas legítimas.
- Resistencia a evasión.
- Integridad de evidencia.
- Latencia añadida.

**Nota estadística:** con 0 fallos en 200, el límite superior aproximado del intervalo unilateral al 95% seguiría rondando el 1,5%. Cero fallos en 200 no prueba una tasa de 0.

## Programa de 90 días

| Fase | Días | Contenido |
| --- | --- | --- |
| 1 — Consolidación | 1–30 | Congelar versiones, modelo de amenazas, preregistro |
| 2 — Ensayos controlados | 31–60 | Ejecución del protocolo |
| 3 — Contraste independiente | 61–90 | Muestra reservada y publicación completa, incluidos los fracasos |

**Criterios de aceptación fijados antes de medir.** Si C no supera a B, se publica el resultado negativo: **si C no supera a B, también es conocimiento útil.**

El preregistro completo está en `CENTRO-001-preregistro.md`.
