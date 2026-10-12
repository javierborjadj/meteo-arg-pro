# 01 — Hoja de Ruta y Etapas del Proyecto (Meteo-Arg-Pro)

**Última actualización:** 12 de octubre de 2026 — **Versión activa:** `v0.9.0`
**Repositorio oficial:** https://github.com/javierborjadj/meteo-arg-pro
**Web pública (GitHub Pages):** https://javierborjadj.github.io/meteo-arg-pro/

---

## Estado General por Etapas

### Etapa 1 — Arquitectura Web Profesional en 3 Secciones y Filtros en Cascada (COMPLETADA)
- [x] Estructura general en 3 secciones independientes (Pestañas de navegación):
  1. `⚡ 1. Tiempo Real & Mapa`
  2. `📅 2. Pronóstico Extendido (24 / 48 / 72 hs)`
  3. `📊 3. Dashboard Auditoría por Localidad`
- [x] Filtros jerárquicos en cascada en la cabecera: **País (Argentina)** -> **Provincia/Región (AMBA activo)** -> **Sub-Localidad puntual (8 zonas)**.
- [x] Unificación estricta de nombres en toda la plataforma:
  - `1. Oficial SMN`
  - `2. Open-Meteo (ECMWF / GFS / ICON)`
  - `3. Modelo Javier (BMA + Kalman + Satélite)`
- [x] Personalización visual: Selector de **4 Paletas de Colores** (Esmeralda, Océano, Cyber, Ámbar) y **Modo Día / Modo Noche** (incluyendo cambio de mapa claro/oscuro).

### Etapa 2 — Verificación en Tiempo Real (Temperatura °C + Agua mm) y Mapa Continuo (COMPLETADA)
- [x] Árbitro en Tierra con estaciones físicas del AMBA (Aeroparque SABE, Obs. Central CABA, Ituzaingó/Morón, Ezeiza, San Fernando, Quilmes, San Miguel, La Plata).
- [x] Cálculo en vivo de doble desvío horario: **Desvío de Temperatura (±°C)** y **Desvío de Agua Caída (±mm)**.
- [x] Medalla dinámica al modelo más preciso del momento y línea inferior de veredicto explicando las diferencias contra el 2° y 3° puesto.
- [x] Mapa con **Campo Continuo de Color (Interpolación Espacial IDW en Canvas)** para Temperatura, Lluvia + Radar RainViewer, Viento y Dirección, Humedad, Satélite NASA GIBS y Riesgo de Fuego.

### Etapa 3 — Pronóstico Extendido y Meteogramas Dobles (COMPLETADA)
- [x] Comparativa a 24, 48 y 72 hs con probabilidad de precipitación (%) separada de milímetros (mm), viento medio y ráfagas.
- [x] Integración del **Sistema de Alerta Temprana (SAT - SMN)** con semáforo de nivel (Verde/Amarillo/Naranja/Rojo).
- [x] Meteograma doble con Chart.js: **Gráfico de Curvas Horarias de Temperatura (°C)** (incluyendo las 5 curvas: Modelo Javier, Oficial SMN, Open-Meteo ECMWF, GFS e ICON) + **Gráfico de Barras Horarias de Agua Estimada (mm)** + Tira horaria deslizable.

### Etapa 4 — Automatización 24/7 en GitHub Actions y Dashboard por Localidad (COMPLETADA)
- [x] Robot automático en GitHub Actions (`.github/workflows/actualizar_datos.yml`) configurado para ejecutarse **cada 1 hora (`10 * * * *`)**.
- [x] Script en Python (`src/motor_meteorologico.py`) que recolecta y guarda hasta **6.000 registros zonales** (~1 mes entero hora por hora) en `data/historial_amba.json`.
- [x] Dashboard por localidad con tarjetas KPI de Error Medio en Temp (±°C) y Agua (±mm), 2 gráficos comparativos, tabla histórica auditable y exportación a Excel (`.CSV`) / importación `.JSON`.

### Etapa 5 — Próximos Pasos y Expansión Nacional (PENDIENTE)
- [ ] Habilitar en el desplegable de Provincias las coordenadas y estaciones árbitro de **Córdoba**, **Santa Fe / Rosario**, **Mendoza** y **Patagonia**.
- [ ] Integrar clave gratuita `MAP_KEY` de **NASA FIRMS** para superponer puntos reales de anomalías térmicas VIIRS (375m) y MODIS (1km).
- [ ] Ajuste automático de pesos históricos en Python leyendo los últimos 30 días de `data/historial_amba.json`.
