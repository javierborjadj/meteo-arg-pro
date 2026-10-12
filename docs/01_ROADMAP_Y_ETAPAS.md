# 01 — Hoja de Ruta y Etapas del Proyecto (Meteo-Arg-Pro)

**Última actualización:** 12 de octubre de 2026
**Región activa actual:** AMBA (CABA + GBA Norte, Oeste y Sur)

## Estado General por Etapas

### Etapa 1 — Prototipo Web Multimodelo y Tiempo Real (COMPLETADA)
- [x] Definición de arquitectura general (`meteo-arg-pro`) escalable a todo el país.
- [x] Selector de regiones de Argentina (AMBA activo; Córdoba, Rosario, Mendoza y Patagonia preparados).
- [x] Tablero en Tiempo Real ("Árbitro en Tierra" vs. Estimaciones horarias).
- [x] Diseño en 3 Columnas comparativas (1. Oficial SMN, 2. Open-Meteo ECMWF vs. GFS, 3. Motor Propio + Satélite).
- [x] Selector de horizonte temporal interactivo (+24 hs, +48 hs, +72 hs).

### Etapa 2 — Mapa Interactivo Multicapa del AMBA (COMPLETADA)
- [x] Mapa base oscuro sin bloqueo local ni API Key (Esri World Dark Gray + Etiquetas de localidades).
- [x] Red de 8 puntos de monitoreo en el AMBA (Aeroparque, Obs. CABA, Ituzaingó/Morón, Ezeiza, San Fernando, Quilmes, San Miguel, La Plata).
- [x] Botones selectores de variables en vivo:
  - [x] 🌡️ Temperatura (con escala térmica de colores).
  - [x] 💨 Viento, Ráfagas y Dirección (con flechas de flujo).
  - [x] 🌧️ Lluvia + Barrido de Radar Meteorológico en vivo (RainViewer).
  - [x] 💧 Humedad Relativa (%).
  - [x] 🛰️ Capa Satelital NASA GIBS.
  - [x] 🔥 Riesgo de Incendio / Monitoreo térmico.

### Etapa 3 — Automatización y Base de Datos de Validación (EN CURSO)
- [x] Estructura de GitHub Actions (`.github/workflows/actualizar_datos.yml`) para ejecución cada 3 horas.
- [x] Script base en Python (`src/motor_meteorologico.py`).
- [ ] Creación y llenado continuo de `data/historial_argentina.sqlite` guardando pronósticos a 24/48/72h sin sobrescribirlos.
- [ ] Cruce automático a fin del día con pluviómetros reales (METAR / SMN) para actualizar el Ranking de Precisión real.

### Etapa 4 — Integración Profunda NASA FIRMS e INMET/GOES (PENDIENTE)
- [ ] Solicitar `MAP_KEY` gratuita en NASA FIRMS para descargar focos VIIRS (375m) y MODIS (1km) reales en Argentina.
- [ ] Integrar alertas oficiales del SMN vía feed público en la Columna 1.
- [ ] Sumar gráficos de evolución horaria (curvas de temperatura y barras de lluvia con Chart.js).
