# 02 — Historial de Versiones y Código (Changelog)

## [v1.1.0] — 2026-10-12 (Paleta Ámbar, Ganador en Naranja, Real en Verde y Ensamble Bates-Granger sin Data Leakage)
### Mejoras agregadas
- **Paleta Ámbar por defecto + Código de Colores Semántico:** El cuadro de la Estación Real queda fijo en **Verde Esmeralda** (`🟢 REAL`) y el cuadro del modelo ganador en ese instante (cualquiera de los 3) se ilumina en **Naranja** (`🟠 🏆 MEJOR AHORA`).
- **Corrección Matemática (Eliminación de Data Leakage):** Se reemplazó la corrección en tiempo real que leía el dato actual por un **Ensamble Bates-Granger de Inversa de Varianza Histórica** (`50% ECMWF + 35% ICON + 15% GFS`, reajustado solo con historial previo).
- **Podio Visual en el Dashboard:** Se reemplazó el texto de conclusión por un tablero de 3 tarjetas de Podio (`🥇 1° Puesto en Naranja`, `🥈 2° Puesto`, `🥉 3° Puesto`).
