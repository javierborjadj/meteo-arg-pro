# 02 — Historial de Versiones y Código (Changelog)

## [v1.2.0] — 2026-10-12 (Transparencia Multimodelo, Ensamble Neutro Inicial y Desempate Exacto)
### Mejoras agregadas
- **Desglose explícito en Cuadro 2 (`2. OPEN-METEO`):** Ahora muestra en vivo el valor individual de `ECMWF`, `GFS` e `ICON` para poder auditar a simple vista la cuenta del Modelo Javier.
- **Metodología Científica de Pesos:** Durante las primeras 24 muestras recolectadas utiliza **Media de Ensamble Equiponderada (`33.3% ECMWF + 33.3% ICON + 33.3% GFS`)** sin porcentajes arbitrarios. Al superar las 24 muestras, activa los pesos dinámicos por Inversa del Error Cuadrático (`1 / MSE`) real medido.
- **Un Único Ganador Naranja (`1° MEJOR AHORA`):** Desempata usando precisión de 2 decimales (`0.01 °C`) para evitar que dos cuadros se iluminen de naranja al mismo tiempo.
