# 02 — Historial de Versiones y Código (Changelog)

## [v0.3.0] — 2026-10-12 (Mapa Multicapa + 8 Zonas del AMBA)
### Mejoras agregadas
- **Mapa Multicapa:** Se añadieron 6 modos interactivos (`temp`, `wind`, `rain`, `hum`, `sat`, `fire`) con leyendas dinámicas y halos zonales.
- **Radar en vivo:** Integración con la API pública de RainViewer para superponer reflectividad de lluvia sobre el AMBA.
- **Muestreo multipunto:** La web consulta en paralelo 8 coordenadas del AMBA para reflejar microclimas entre la costa (Aeroparque/Quilmes) y el oeste/sur (Ituzaingó/Morón/Ezeiza).
### Problemas corregidos (Bugfixes)
- **Fix Error 403 OpenStreetMap:** Al abrir `index.html` vía `file://`, OSM bloqueaba los tiles por falta de `Referer`. Se migró a **Esri ArcGIS Dark Gray Canvas + Reference**, que funciona tanto en local como en servidor.

## [v0.2.0] — 2026-10-12 (Conexión de APIs en Vivo y Fix PowerShell)
### Problemas corregidos
- **Fix de variables `$` en PowerShell:** Se cambió el bloque generador de `@"..."@` a `@'...'@` para evitar que Windows borrara las variables de JavaScript.
- **Consultas separadas ECMWF y GFS:** Se conectaron los endpoints `/v1/ecmwf` y `/v1/gfs` de Open-Meteo para obtener curvas reales a 24, 48 y 72 hs.

## [v0.1.0] — 2026-10-12 (Estructura Inicial Meteo-Arg-Pro)
- Creación del árbol de directorios (`src/`, `data/`, `.github/workflows/`, `docs/`).
- Diseño de interfaz oscura con Tailwind CSS, 3 columnas comparativas y panel de verificación en tiempo real.
