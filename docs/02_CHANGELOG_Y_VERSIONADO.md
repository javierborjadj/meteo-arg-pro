# 02 — Historial de Versiones y Código (Changelog)

## [v1.3.0] — 2026-10-12 (Fix Bug Datos de Respaldo, Cortes Horarios :00 hs y Reconstrucción 24 hs Reales)
### Problemas corregidos y mejoras
- **Fix Bug 16.7 °C en ECMWF:** Se eliminó el guardado prematuro de datos de respaldo antes de que respondieran las APIs reales. Ahora la tabla solo registra mediciones provenientes de respuestas reales (`200 OK`) de Open-Meteo.
- **Cortes Horarios Estrictos (`:00 hs`):** La tabla de auditoría registra exactamente 1 corte por hora cerrada (`00:00 hs`, `01:00 hs` ... `19:00 hs`) en lugar de guardar minutos sueltos (`19:21`, `19:22`).
- **Backfill Horario Automático del Día:** Al iniciar, reconstruye las 20 horas cerradas transcurridas del día usando las series horarias reales de ECMWF, ICON y GFS contra las observaciones.
