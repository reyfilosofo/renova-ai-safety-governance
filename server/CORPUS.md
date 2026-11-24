# Corpus del servidor MCP ℛenova

El servidor lee su corpus de rutas configurables por variables de entorno.
`start.sh` ya las apunta a la raíz de este repositorio.

| Variable | En este repo | Qué es |
|---|---|---|
| `RENOVA_STAGING_DIR` | La raíz del repo (`docs/`, `benchmark/`, `centro-guard-policy.yaml`, `README.md`, `packages/PACKAGES.md`) | Contenido canónico del espacio RENOVA AI SAFETY & GOVERNANCE v6 (10 nov 2026), contenido unificado 17 nov 2026: 3 documentos fundacionales verbatim, política CENTRO Guard RNV-01–RNV-06, Benchmark ℛ v0.1 (R-001–R-040) y preregistro CENTRO-001 (borrador). |
| `RENOVA_INVENTARIO_JSON` | `renova-fundamento-inventario-drive.json` (93 KB) | Metadatos verificados de las 54 obras de Fundamento (28 de Drive + 11 del chat + 16 de la Biblioteca, con enlaces a Drive). Solo metadatos, no texto completo. |
| `RENOVA_BIBLIOTECA_DIR` | **No incluido** | Texto extraído de las 24 obras de la Biblioteca (4.478 págs., 1.869.502 palabras). No se incluye por tamaño y por derechos de los libros. Para activarlo, clona o copia esa carpeta y apunta la variable. Sin ella, el servidor degrada con gracia: `renova_search` cubre staging + metadatos de Fundamento y lo declara en la cobertura. |
| `RENOVA_DATA_DIR` | `server/data/` (se crea al usarlo) | Registro local LUCEM (`lucem.jsonl`, hash encadenado). Nunca se sube: está en `.gitignore`. |

El servidor nunca inventa texto de libros que no leyó: el texto completo de
las 28 obras de Drive y las 11 del chat no está indexado por diseño declarado.

Nota de fidelidad: `renova_get_state` cuenta las 24 obras de la Biblioteca
por metadatos aunque su texto no esté cargado (entonces
`biblioteca_24_words` es 0). La cobertura real se ve por resultado en
`renova_search` (`coverage: texto_completo_extraido` o metadatos).

## Método (resumen)

- **Búsqueda:** texto completo sobre staging + Biblioteca (si está cargada)
  + metadatos de Fundamento. Cada resultado declara su fuente y su cobertura.
- **CENTRO Guard:** RNV-01 a RNV-06 leídas de `centro-guard-policy.yaml`
  (versión 1.0, propuesta de diseño). Veredictos simulados: DENY, REVIEW o
  ALLOW_SIMULATED. Ninguno ejecuta ni bloquea una acción real.
- **Benchmark ℛ v0.1:** escenarios R-001–R-040 parseados del diseño
  (`benchmark/benchmark-r-v0.1-diseno-y-lote-inicial.md`). `gold_label`
  siempre null: la revisión ciega (Revisor A, Revisor B, adjudicador
  independientes del autor) está pendiente. La etiqueta de autor es una
  propuesta, no una verdad de referencia.
- **EGRA:** compara tratamiento contra baseline solo con puntuaciones
  explícitas; si faltan, devuelve `incompleto_sin_datos` y no las inventa.
- **LUCEM:** registro local de evidencia con hash encadenado SHA-256.
- **Falsabilidad:** CENTRO-001 / RENOVA T-001 es el experimento que
  decidiría si CENTRO Guard reduce ejecuciones no autorizadas frente a
  un control convencional. Es un preregistro propuesto, no ejecutado,
  sin resultados. Si el grupo C no supera al B, el resultado negativo
  también se publica.
