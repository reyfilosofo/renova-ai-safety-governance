# Simulador Guard

> La versión interactiva de este simulador vive en el espacio RENOVA AI SAFETY & GOVERNANCE en Muse. Este documento recoge sus reglas. **El simulador no ejecuta ni bloquea nada real: la evidencia que muestra es SIMULADA.**

## Regla de decisión

El usuario configura una solicitud — operación, recurso, identidad verificada fuera del modelo, permiso, evidencia y clase de reversibilidad — y Guard devuelve **ALLOW**, **DENY** o **ASK** aplicando la regla más estricta: **DENY sobre ASK sobre ALLOW**.

**Reformular la solicitud no cambia la decisión** si la operación, el recurso y el efecto son los mismos: una operación prohibida no se vuelve permitida porque el modelo reformule su solicitud.

## Controles

- **Operación:** Leer, Escribir, Publicar, Eliminar, Transferir.
- **Recurso:** Documentación pública, Archivo propio, Archivo privado, Base documental, Servidor externo, Dinero.
- **Identidad verificada fuera del modelo:** Sí / No.
- **Permiso:** Específico y vigente, Ambiguo, Ausente, Falsificado.
- **Evidencia:** Confirmada, Faltante, Inferida, No verificable.
- **Reversibilidad:** R0 Reversible, R1 Reparable, R2 Irreversible, R3 Propagación.

## Clases de reversibilidad

- **R0 Reversible** — leer, consultar sin cambiar el estado.
- **R1 Reparable** — escribir con control de versiones o copia.
- **R2 Irreversible** — eliminar sin copia, sobrescribir sin respaldo.
- **R3 Propagación** — publicar, enviar o exfiltrar. Lo divulgado no vuelve a ser secreto con un rollback.

## Estados de la evidencia

- **Confirmada** — verificable por un componente independiente; puede sustentar ALLOW.
- **Faltante** — DENY en R2 y R3.
- **Inferida** — nunca basta para ALLOW en R2 y R3. La confianza no es autorización.
- **No verificable** — se trata como faltante.

## Presets

1. **Leer documentación pública** — ALLOW (lectura acotada, identidad válida, sin efecto externo).
2. **Publicar archivo privado sin permiso específico** — DENY (permiso ausente y propagación de archivo privado).
3. **Eliminar recurso sin copia** — DENY (R2, irreversible sin respaldo).
4. **Escribir con control de versiones y permiso vigente** — ALLOW.
5. **Transferir dinero con permiso ambiguo** — ASK (permiso ambiguo, efecto externo con dinero).

## Límites del simulador

- Decide en el navegador a partir de reglas; no hace cumplir nada real.
- La evidencia mostrada (por ejemplo, el hash) es simulada.
- No sustituye a CENTRO Guard: un DENY del simulador no impide que un agente con acceso directo a la herramienta actúe. Un DENY solo es preventivo si es vinculante.
