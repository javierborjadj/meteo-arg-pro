# 🛰️ Meteo-Arg-Pro (`v0.9.0`)

Plataforma meteorológica multimodelo y de auditoría en tiempo real para Argentina (Región activa inicial: **AMBA — CABA + Gran Buenos Aires**).

🔗 **Ver aplicación web en vivo:** [https://javierborjadj.github.io/meteo-arg-pro/](https://javierborjadj.github.io/meteo-arg-pro/)

## Características principales
1. **⚡ Tiempo Real & Mapa Continuo:** Compara termómetros y pluviómetros reales en tierra contra **1. Oficial SMN**, **2. Open-Meteo (ECMWF/GFS/ICON)** y **3. Modelo Javier (BMA + Kalman + GOES)**, midiendo tanto el desvío de **Temperatura (°C)** como el de **Agua Caída (mm)**.
2. **📅 Pronóstico Extendido (24 / 48 / 72 hs):** Meteogramas horarios dobles (curvas de temperatura y barras de lluvia) y alertas del SMN.
3. **📊 Dashboard de Auditoría por Localidad:** Recolección automática **cada 1 hora vía GitHub Actions** en `data/historial_amba.json` (hasta 6.000 registros) con exportación a Excel (`.CSV`).

📁 Toda la documentación técnica y de versiones se encuentra en la carpeta [`docs/`](./docs/).
