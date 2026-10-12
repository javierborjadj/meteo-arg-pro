# 02 — Historial de Versiones y Código (Changelog)

## [v1.5.0] — 2026-10-12 (Expansión Multi-Provincial: AMBA, PBA Interior, Córdoba, Santa Fe, Entre Ríos, Tucumán y Salta)
### Mejoras agregadas
- **7 Provincias / Regiones Activas:** Se habilitaron las coordenadas, estaciones oficiales y sub-localidades en cascada para:
  1. `AMBA (CABA + GBA)` — 8 localidades
  2. `Provincia de Buenos Aires (Interior)` — Mar del Plata, Bahía Blanca, Tandil, Junín, Pergamino, Necochea
  3. `Córdoba` — Córdoba Capital, Río Cuarto, Villa Carlos Paz, Villa María, San Francisco
  4. `Santa Fe` — Rosario, Santa Fe Capital, Rafaela, Venado Tuerto, Reconquista
  5. `Entre Ríos` — Paraná, Concordia, Gualeguaychú, Concepción del Uruguay
  6. `Tucumán` — San Miguel de Tucumán, Yerba Buena, Tafí del Valle, Concepción
  7. `Salta` — Salta Capital, Cafayate, Orán, Tartagal
- **Cálculo y Mapa Regional Automático:** Al elegir una provincia, el mapa animado de Windy y el de estaciones hacen foco en esa provincia, el motor consulta en vivo las curvas de ECMWF, GFS e ICON para esa región y reconstruye las 24 horas de auditoría provincial.
