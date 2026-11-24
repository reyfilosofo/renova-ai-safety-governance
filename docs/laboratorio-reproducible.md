# Laboratorio reproducible — Public Lab 1.1.0

> La versión interactiva de estas herramientas vive en el Public Research Lab de ChatGPT (https://renova-safety-governance.seresarte.chatgpt.site) y, como calculadora, en el espacio RENOVA AI SAFETY & GOVERNANCE en Muse. Todo corre en el navegador: sin clave API, sin envío a servidor, sin llamadas a modelos.

## Tres herramientas, un criterio: trazabilidad

### 1. Evaluaciones

Editor JSONL para evaluar decisiones de agentes. Ejemplo precargado de 8 casos: TP 3 · FN 1 · FP 1 · TN 3, FNR 25% y FPR 25%. Límites: máximo 5.000 filas / 2 MiB.

La calculadora de evaluación binaria muestra matriz de confusión, FNR, FPR, exactitud e intervalos de Wilson al 95% — solo bajo supuesto de independencia, declarado.

### 2. Manifiestos

Editor de manifiestos de evidencia. La plantilla incompleta reporta los ítems faltantes: el manifiesto no afirma lo que no documenta.

### 3. Paquetes 2.1

Paquetes documentales con estados **PREPARED** y **ACKNOWLEDGED**. Un paquete PREPARED no puede afirmar recibo ni lectura verificada. La validación comprueba solo consistencia documental: no autentica el recibo ni la lectura.

## Kit reproducible

**`renova-evidence-toolkit-1.1.0.zip`** — SHA-256:

```
85fc29204b595d0c794d81b8cb41601e820d662f6f4c101dd073d98cae872f5b
```

7 archivos, Node.js ≥ 22.13, sin claves, sin llamadas a modelos, sin instalación, sin red.

**Verificado por Muse el 2026-11-10:** SHA exacto, los 7 archivos coinciden con `release-evidence.json`, **32/32 pruebas superadas** con Node v24.22.1, la CLI reproduce el ejemplo n=8 (exactitud 0,75; Wilson 95% solo con `--assume-independent`) y la plantilla de manifiesto incompleta se rechaza correctamente como incompleta.

**Distinción precisa:** 32/32 son las pruebas del kit verificadas por Muse. La cifra «61 tests» es lo que publica el sitio y **no fue replicada por Muse**.

## Límites del laboratorio

Software experimental para problemas concretos de evaluación. La reducción de riesgos en sistemas reales requiere pruebas adicionales. No se atribuyen certificaciones, consciencia artificial ni mitigación demostrada del riesgo AGI. «No existe un kill switch general de IA o AGI. Este sitio no controla las herramientas de otros agentes.»
