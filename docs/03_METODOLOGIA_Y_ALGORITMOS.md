# 03 — Metodología, Cálculos y Algoritmos del Modelo Javier (v0.9.0)

## 1. Doble Árbitro en Tierra: Temperatura (°C) y Agua Caída (mm)
Para cada una de las 8 sub-localidades del AMBA se evalúan en simultáneo dos errores absolutos respecto de las estaciones oficiales:
- **Error Térmico Horario:** `Err_Temp = |Temp_Estimada - Temp_Real_Estacion|` (en °C).
- **Error Pluviométrico Horario:** `Err_Agua = |Agua_Estimada - Agua_Real_Pluviometro|` (en mm).
- **Puntaje Combinado de Precisión (Score):** `Score = Err_Temp + (1.5 * Err_Agua)`. El modelo con menor puntaje combinado recibe la insignia de mayor precisión en ese estado.

## 2. Fórmulas Matemáticas del "3. Modelo Javier"
1. **Bayesian Model Averaging (BMA) / Inversa del Error Cuadrático:**
   Pondera en vivo las 3 supercomputadoras consultadas vía Open-Meteo (`ECMWF`, `ICON`, `GFS`) según su error cuadrático frente al árbitro:
   `w_i = (1 / (Error_Base_i^2 + (T_i - T_Real)^2)) / Suma_Total`
2. **Filtro de Decaimiento Exponencial (Nowcasting tipo Kalman):**
   Mide el sesgo en la hora 0 (`Bias_0 = T_Real - T_BMA`) y ajusta la curva horaria con constante de decaimiento `tau = 6 hs`:
   `T_Javier(t) = T_BMA(t) + Bias_0 * exp(-t / 6)`
3. **Refuerzo No Lineal Hydro-Estimator (Satélite GOES / INMET):**
   Cuando el tope nuboso infrarrojo cae por debajo de `-45 °C`, aplica el factor convectivo `1 + 0.18 * ((-45 - T_IR) / 25)^1.4`.
4. **Índice de Peligro de Incendio de Angström:**
   `I = (Humedad_% / 20) + ((27 - Temp_C) / 10) - (0.05 * Viento_kmh)`. Si `I < 2.5`, el riesgo es Crítico (Rojo).

## 3. Interpolación Espacial del Mapa (IDW — Inverse Distance Weighting)
Para pintar todo el mapa con colores continuos (calor, agua, viento, humedad, fuego), el motor Canvas calcula en cada celda de la pantalla el promedio ponderado por la cuarta potencia de la inversa de la distancia (`w = 1 / (d^2 + c)^2`) hacia las 8 estaciones del AMBA.
