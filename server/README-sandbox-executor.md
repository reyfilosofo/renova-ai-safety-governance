# Ejecutor de sandbox vinculante — CENTRO-001 (prototipo)

**Estado: PROTOTIPO local. No es el prototipo registrado de CENTRO-001.**
El prototipo que se evalúa en el experimento lo decide Rey (decisiones
D2/D3 del preregistro propuesto,
`CENTRO-001-preregistro.md` en la raíz del repo).
Este módulo es trabajo de preparación de la fase 1 (días 1–30) y nada más.
No se despliega, no se registra, no se publica, no gasta nada.

## Nota de subida al repo — 25 de noviembre de 2026

Este prototipo se escribió el 24 de noviembre de 2026 en el workspace local de Muse y se sube al repo el 25 de noviembre de 2026 para que un externo pueda inspeccionarlo: la auditoría integral de ChatGPT (25 nov 2026) no pudo verificarlo porque no estaba en el repo. **29 pruebas stdlib, 0 fallos** (verificadas 24 nov 2026; re-verificadas tras ajustar las rutas al repo). **NO desplegado**: no es el prototipo registrado de CENTRO-001 (eso lo decide Rey, D2/D3).

Huecos declarados (sin cambios): `SEND`, `DEPLOY`, `PURCHASE` y `PHYSICAL_ACTUATE` no tienen efecto confinado definido y no se ejecutan aunque el gate las deje en `REVIEW` con aprobación humana (motivo `NO_CONFINED_EFFECT_DEFINED`); un solo proceso no es una frontera de seguridad (la separación de procesos es trabajo de la fase 1).

Ajustes de rutas para el repo (sin tocar la lógica): las referencias a `~/workspace/renova-mcp-server/` pasan a `server/`; la procedencia del gate ahora apunta a `packages/RENOVA_AI_SAFETY_GOVERNANCE_STACK_V2_0_2026-11-09.zip`; `GATE_SOURCE_ZIP` se resuelve desde la ubicación del módulo para que la prueba de procedencia funcione se corra desde donde se corra.

## Qué es

Un sandbox mínimo en el que las «acciones» son operaciones de archivo
(`WRITE` / `READ` / `RETRIEVE` / `EVALUATE` / `DELETE`) confinadas a un
directorio temporal que se limpia al terminar. Cada acción pasa
obligatoriamente por el gate ActionGate del stack RENOVA v2.0, vendado
verbatim en `sandbox_executor.py` con su procedencia y sus hashes
SHA-256 (verificables con el test de procedencia).

Reglas que aplica el ejecutor, sin excepción:

| Veredicto del gate | Efecto |
| --- | --- |
| `DENY` | Nunca se ejecuta. Ni siquiera con `human_approval=True`. |
| `REVIEW` | Solo se ejecuta con `human_approval=True` en esa llamada. La aprobación vale para una llamada, no es persistente. |
| `ALLOW_SIMULATED` | Se ejecuta. El efecto es real pero confinado al sandbox. |

Cada intento — permitido, denegado, en revisión, rechazado por ruta —
queda registrado en JSONL con hash encadenado, con el mismo sobre que
usa LUCEM en `renova_core.py` (`id`, `timestamp_utc`, `entry`, `source`,
`tags`, `prev_hash`, `hash`). El registro vive en
`<sandbox>/.lucem/lucem.jsonl` y se borra con el sandbox al cerrar:
para conservar la evidencia hay que llamar a `export_log(ruta)` o a
`read_log()` antes de cerrar.

## Qué NO es

- **No es una garantía de seguridad.** Es un prototipo en un solo
  proceso de Python. La vinculación es estructural frente a cualquier
  llamador que use la API pública, pero no frente a un llamador que
  reescriba los internals del ejecutor en el mismo proceso (ver
  «Límites honestos» abajo).
- **No ejecuta nada real fuera del sandbox.** Los efectos existen solo
  dentro del directorio temporal.
- **No cubre todas las operaciones.** `SEND`, `DEPLOY`, `PURCHASE` y
  `PHYSICAL_ACTUATE` no tienen efecto confinado definido en este
  prototipo: aunque el gate las deje en `REVIEW` y haya aprobación
  humana, no se ejecutan y quedan registradas con el motivo
  `NO_CONFINED_EFFECT_DEFINED`. Es un hueco declarado, no un efecto
  simulado a escondidas.
- **No es el servidor MCP.** No modifica ningún archivo existente del servidor. Es un módulo nuevo e independiente.

## Cómo se garantiza la vinculación

No es por convención («por favor, pasa por el gate»). Es estructural:

1. **No existe ninguna función pública que ejecute un efecto.** El
   módulo solo exporta `SandboxExecutor`, `Action` y `BindingError`.
2. **`execute()` es el único punto de entrada y no acepta un veredicto
   como parámetro**: llama al gate él mismo. Un llamador no puede
   falsificar un `ALLOW`.
3. **Capacidad de un solo uso**: las funciones de efecto (métodos
   privados `_effect_*`) exigen un objeto opaco creado dentro de
   `execute()` solo después de un veredicto que autoriza, vivo
   únicamente durante esa llamada y borrado en `finally`. Una llamada
   directa con una capacidad falsificada, `None` o ya consumida falla
   con `BindingError` sin efecto.
4. **La raíz del sandbox solo la conoce la instancia.** Las rutas se
   resuelven contra ella y se rechaza cualquier escape: rutas
   absolutas, `..`, enlaces simbólicos que apunten fuera, y el
   directorio de evidencia `.lucem/` está vedado a las acciones.
5. **`bypass_probe()`** ejecuta la prueba de vinculación que exige el
   preregistro (§6): intenta las rutas de bypass conocidas y reporta
   por ruta si quedó bloqueada. Antes de la primera corrida válida de
   CENTRO-001, todas deben dar `blocked: True`.

## Cómo correr las pruebas

Desde `server/`:

```bash
python3 -m unittest test_sandbox_executor -v
```

Stdlib, sin dependencias. Resultado verificado el 2026-11-24:
**29 pruebas, 0 fallos.** Cubren: DENY nunca ejecutado (ni con
aprobación humana, ni por llamada directa con capacidad falsificada);
ALLOW ejecutado solo dentro del sandbox; REVIEW sin flag no ejecutado
y con flag sí (flag por llamada, no persistente); todos los intentos
registrados en JSONL con cadena de hashes verificada; nada escrito
fuera del directorio temporal (incluidos traversal, ruta absoluta,
enlace simbólico y escritura al directorio de evidencia); operaciones
sin efecto confinado no ejecutadas; procedencia del gate byte-idéntica
al zip original; cierre y limpieza del sandbox.

Ejemplo de uso:

```python
from sandbox_executor import Action, SandboxExecutor

with SandboxExecutor(allowed_resources={"notes/a.txt"}) as ex:
    r = ex.execute(Action("WRITE", "notes/a.txt", content="hola"),
                   human_approval=True)   # REVIEW + aprobación -> ejecuta
    print(r["executed"], r["verdict"])     # True REVIEW
    r = ex.execute(Action("READ", "notes/a.txt"))
    print(r["effect"]["content"])          # "hola"
    print(ex.bypass_probe())               # todas blocked: True
    ex.export_log("/tmp/evidencia-centro-001.jsonl")  # antes de cerrar
```

## Qué falta para usarlo en CENTRO-001 (decisiones de Rey)

1. **D2 — prototipo.** Rey decide si este ejecutor + ActionGate es el
   prototipo que se congela, o si se usa otro. Hasta entonces, esto es
   preparación, no el prototipo registrado.
2. **D3 — agente ejecutor.** La propuesta es un harness determinista
   guionado (sin LLM). Este módulo no incluye el harness: solo el
   gate + ejecutor. El harness debe construirse en la fase 1 y llamar
   a `execute()` con un escenario por vez.
3. **Efectos confinados para SEND / DEPLOY / PURCHASE /
   PHYSICAL_ACTUATE.** Hoy esas operaciones no se pueden medir como
   «ejecutadas». Para medirlas hace falta definir su efecto confinado
   (p. ej. un outbox dentro del sandbox para SEND) y registrar esa
   decisión en el preregistro antes del congelamiento. Sin eso, los
   escenarios de esas operaciones solo miden el veredicto del gate,
   no la ejecución.
4. **Separación de procesos.** La vinculación real frente a un agente
   adversario exige que el gate viva en un proceso distinto del
   agente, sin credenciales ni rutas alternativas para el agente
   (preregistro §3, «condición decisiva»). Este módulo, en un solo
   proceso, es el núcleo lógico; el despliegue en dos procesos es
   trabajo de la fase 1.
5. **Congelamiento.** En los días 1–30 se congelan la versión exacta
   del gate y del ejecutor (commit + SHA-256) y se registra como
   adenda fechada antes del día 31. Ningún cambio de código después
   sin una versión nueva del experimento.

## Límites honestos

- **L1. Un proceso no es una frontera de seguridad.** Quien pueda
  reasignar `executor._live_capability` o `executor._effect_write`
  en el mismo proceso puede eludir el gate. Eso equivale a reescribir
  el control, no a usarlo. La prueba de bypass cubre las rutas de un
  llamador que usa la API; no cubre la reescritura deliberada de
  internals. La separación de procesos (punto 4 de arriba) es lo que
  cierra ese hueco.
- **L2. El gate es consultivo por diseño.** Su docstring lo dice:
  «Offline-only advisory gate… no side-effect executor». La
  vinculación la aporta este ejecutor, no el gate. Usar el gate solo
  vuelve a ser consultivo.
- **L3. `ALLOW_SIMULATED` es autorización simulada en el vocabulario
  del gate.** Dentro del sandbox el efecto sí se aplica de verdad,
  pero solo dentro del sandbox. No es autorización en ningún sistema
  externo.
- **L4. Rama inalcanzable del gate.** `assess()` contempla
  `DENY / UNKNOWN_OPERATION` para operaciones desconocidas, pero los
  contratos las rechazan antes de que el gate las vea. Defensa en
  profundidad, no camino ejecutable.
- **L5. El registro se pierde si se olvida exportarlo.** El JSONL vive
  dentro del sandbox y se borra al cerrar. `export_log()` antes de
  cerrar, o `read_log()` en memoria.
- **L6. Sin reloj ni identidad externos.** `timestamp_utc` es el reloj
  del sistema y la identidad la aporta quien construye el ejecutor.
  En CENTRO-001 la identidad debe venir de fuera de banda, como
  exigen los contratos del stack.

## Archivos

- `sandbox_executor.py` — el módulo (gate vendado + ejecutor + registro).
- `test_sandbox_executor.py` — 29 pruebas stdlib unittest.
- `README-sandbox-executor.md` — este archivo.

Ningún archivo existente del servidor fue modificado.
