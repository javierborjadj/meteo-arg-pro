# 02 — Historial de Versiones y Código (Changelog)

## [v0.9.0] — 2026-10-12 (Menús en Cascada, Modo Día/Noche, Paletas, Carga Garantizada y Robot Horario)
### Mejoras agregadas
- **Filtros en Cascada:** Separación en 3 menús independientes (`País: Argentina` -> `Provincia/Región: AMBA` -> `Sub-Localidad puntual`).
- **Temas y Paletas:** Selector de 4 paletas de acento CSS y botón **Modo Día / Modo Noche** que alterna también los tiles del mapa entre *Esri Dark Gray* y *Esri Light Gray*.
- **Motor Tolerante a Fallos (`Promise.allSettled` + Semilla Inicial):** Carga instantánea en 0.1s para evitar valores en `--` si una API externa demora, y renderizado seguro de gráficos al cambiar de pestaña.
- **Robot de GitHub cada 1 Hora:** Actualización del cron de GitHub Actions a `10 * * * *` (24 corridas diarias) y ampliación del historial en Python a 6.000 registros en `data/historial_amba.json`.

## [v0.8.0] — 2026-10-12 (Arquitectura en 3 Secciones + Auditoría Doble Temperatura y Agua)
### Mejoras agregadas
- División de la interfaz en 3 vistas: `1. Tiempo Real & Mapa`, `2. Pronóstico Extendido`, `3. Dashboard Auditoría`.
- Incorporación del **Desvío de Agua (±mm)** en tarjetas de tiempo real, línea de veredicto, meteograma de barras de lluvia y tabla del Dashboard.
- Funciones de exportación a Excel (`.CSV`) e importación de `.JSON`.

## [v0.7.0] — 2026-10-12 (Unificación de Nombres + Mapa de Color Continuo IDW)
### Mejoras agregadas
- Unificación de etiquetas en toda la web: `1. Oficial SMN`, `2. Open-Meteo (ECMWF/GFS/ICON)` y `3. Modelo Javier`.
- Inclusión de la curva `1. Oficial SMN` en el meteograma horario.
- Creación de la capa `CapaCampoColorContinuo` en Canvas HTML5 sobre Leaflet mediante **Interpolación Espacial IDW** para pintar el mapa completo con gradientes de calor, lluvia, viento, humedad y riesgo de fuego.

## [v0.6.0] — 2026-10-12 (Modelo Javier + Ganador Dinámico Honesto + Guardado Local)
- Renombrado oficial de la Columna 3 a **Modelo Javier**.
- Cálculo dinámico de la medalla `🏆 MÁS PRECISO AHORA` y línea inferior de veredicto con diferencias exactas en grados.
- Primer sistema de persistencia en `localStorage` por localidad del AMBA.

## [v0.5.0] — 2026-10-12 (Modelos Matemáticos BMA + Kalman + Angström + 3er Modelo ICON)
- Incorporación del modelo alemán **DWD ICON** junto a **ECMWF** y **NOAA GFS**.
- Programación de pesos dinámicos **BMA**, corrección de sesgo exponencial **Kalman-like** e **Índice Forestal de Angström**.
- Banner del Sistema de Alerta Temprana (**SAT - SMN**).

## [v0.1.0 a v0.4.0] — 2026-10-12 (Prototipo Base, Fix PowerShell, Mapa Esri y Relojes Individuales)
- Estructura inicial del proyecto, solución de variables `$` en PowerShell, migración a mapas Esri sin bloqueo 403 y estampado de fecha/hora de actualización en cada tarjeta.
