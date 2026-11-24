# Benchmark ℛ

Benchmark bilingüe y multicultural (es-MX / en) de RENOVA AI SAFETY & GOVERNANCE. Mide si una autoridad externa al modelo —CENTRO / ActionGate— reduce las acciones no autorizadas que un agente llega a **ejecutar**, frente a un agente sin esa autoridad, en un sandbox offline y sin participantes humanos.

## Archivos

| Archivo | Contenido |
| --- | --- |
| `benchmark-r-v0.1-diseno-y-lote-inicial.md` | Diseño completo de Benchmark ℛ v0.1 (verbatim): pregunta, hipótesis falsable H1/H0, taxonomía de 10 categorías, lote inicial R-001–R-040 con etiquetas propuestas del autor, splits, métricas y umbrales declarados antes de correr |

## Estado

- **v0.1 es un diseño con un lote inicial de escenarios. No es un resultado.**
- Lote inicial: 40 escenarios (20 es-MX, 20 en; 17 `DENY`, 15 `REVIEW`, 8 `ALLOW_SIMULATED` como etiquetas propuestas del autor). Todas las `gold_label` están en `null` hasta completar la revisión ciega.
- El lote v0.1 nace en dev y nunca pasará al split sellado, porque su contenido ya es público desde su diseño.
- Meta del benchmark completo: 100–200 escenarios congelados (dev 60 / validación 40 / prueba sellada 60).

## Pendiente

- **Revisión ciega:** sin Revisor A, Revisor B ni adjudicador nombrados, todos independientes del autor de la política. Hasta que existan, el benchmark no pasa de la fase dev.
- **Lote legible por máquina:** no existe todavía un archivo JSON/JSONL con los escenarios R-001–R-040 en el workspace; los escenarios viven en la tabla del documento de diseño. La v0.2 deberá publicar `benchmark-r-v0.1-scenarios.jsonl` generado a partir de esa tabla, sin cambiar su contenido.
- **Ejecutor de sandbox y primera corrida dev:** pendientes (plan v0.3).

## Límites

Un resultado positivo en Benchmark ℛ sería evidencia sobre **este** gate, en **este** sandbox, contra **estos** escenarios. No sería validación externa de RENOVA en producción. Resultado sintético no es validación externa, también cuando el sintético es este benchmark en su fase dev.
