# 02 — Historial de Versiones y Código (Changelog)

## [v1.0.0] — 2026-10-12 (Mapa Animado ECMWF/Windy, Filtro de Fechas, Conclusión Automática y UI Clara)
### Mejoras agregadas
- **Doble Motor de Mapa:** Se integró el **Mapa de Calor y Partículas Animadas (Windy / ECMWF / GFS)** idéntico al estilo profesional de Meteored, conmutable con el **Mapa de 8 Estaciones Puntuales del AMBA** con escala de contraste dinámico.
- **Traducción de Indicadores Satelitales:** Se reemplazó el valor crudo de temperatura de tope nuboso en altura (`-57.0 °C`) por estados claros (`🟢 Cielo despejado / Nubes bajas`, `🟡 Nubosidad media`, `🟠 Nubes altas de tormenta`).
- **Marcador Resumido en Tiempo Real:** Se sintetizó el veredicto en 2 tarjetas cortas (`🌡️ Líder Temperatura` y `🌧️ Líder Agua Caída`).
- **Filtro de Fechas (`Desde 2026-10-12` — `Hasta hoy`) y Conclusión Automática en Dashboard:** El Dashboard redacta automáticamente qué modelo fue superior en la localidad y rango de fechas elegidos.
