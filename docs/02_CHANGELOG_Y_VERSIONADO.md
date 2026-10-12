# 02 — Historial de Versiones y Código (Changelog)

## [v1.4.0] — 2026-10-12 (Separación y Auditoría Completa de los 5 Modelos en Dashboard, Gráficos y Tabla)
### Mejoras agregadas
- **Los 5 Modelos compiten separados de punta a punta:** Se desglosó `2. Open-Meteo` en sus 3 modelos constituyentes dentro del Dashboard, los gráficos y la tabla histórica:
  1. `1. Oficial SMN`
  2. `2A. Open-Meteo (ECMWF Europeo)`
  3. `2B. Open-Meteo (GFS EE.UU.)`
  4. `2C. Open-Meteo (ICON Alemán)`
  5. `3. Modelo Javier (Ensamble Bates-Granger)`
- **5 Tarjetas de Clasificación en el Dashboard:** Muestra del 1° al 5° puesto con victorias horarias, error medio de temperatura (`±°C`) y error medio de agua (`±mm`).
- **Tabla Horaria y Exportación CSV de 5 Columnas:** Permite ver exactamente en qué horas del día ganó GFS, en cuáles ganó ICON, en cuáles ECMWF y en cuáles el Modelo Javier.
