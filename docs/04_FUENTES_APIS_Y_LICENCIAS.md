# 04 — Catálogo de Fuentes, APIs y Automatización en GitHub (v0.9.0)

## 1. Fuentes de Datos Activas

| Nombre en Plataforma | Fuente Técnica / Endpoint | Frecuencia | Requiere API Key |
| :--- | :--- | :--- | :---: |
| **🎯 Árbitro Estaciones** | Red Oficial SMN / NOAA AviationWeather METAR (`SABE`, `SADM`, `SAEZ`, `SADF`, `SADL`) + Muestreo Zonal | Horaria | No |
| **1. Oficial SMN** | Servicio Meteorológico Nacional (Pronóstico Zonal y Sistema de Alerta Temprana SAT) | Cada 1 a 6 hs | No |
| **2. Open-Meteo (ECMWF)** | `/v1/ecmwf` — Centro Europeo de Predicción a Plazo Medio | Horaria (4 días) | No |
| **2. Open-Meteo (GFS)** | `/v1/gfs` — Modelo Global NOAA (EE.UU.) | Horaria (4 días) | No |
| **2. Open-Meteo (ICON)** | `/v1/dwd-icon` — Servicio Meteorológico Alemán (DWD) | Horaria (4 días) | No |
| **🌧️ Radar en Vivo** | RainViewer Public Weather Maps API | Cada 10 min | No |
| **🛰️ Satélite NASA** | NASA GIBS WMTS (`MODIS_Terra_CorrectedReflectance`) | Diaria / Regional | No |
| **🗺️ Mapa Base Día/Noche** | Esri ArcGIS Online (`World_Dark_Gray` y `World_Light_Gray`) | Continua | No |

## 2. Flujo de Trabajo y Automatización 24/7 en GitHub
- **Repositorio:** `https://github.com/javierborjadj/meteo-arg-pro`
- **Agente Recolector (`actualizar_datos.yml`):** Corre automáticamente en los servidores de GitHub en el **minuto 10 de cada hora (`10 * * * *`)**, ejecuta `python src/motor_meteorologico.py` y guarda las mediciones de las 8 zonas del AMBA en `data/historial_amba.json` (conservando hasta 6.000 registros).
