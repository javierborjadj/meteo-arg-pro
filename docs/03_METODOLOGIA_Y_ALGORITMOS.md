# 03 — Metodología, Cálculos y Modelos Matemáticos (v0.5.0)

## 1. Bayesian Model Averaging (BMA) / Ponderación por Inversa del Error Cuadrático
- Integra **3 modelos globales independientes**: **ECMWF** (Europa), **DWD ICON** (Alemania) y **NOAA GFS** (EE.UU.).
- El peso dinámico de cada modelo se recalcula en función de su error cuadrático frente a las estaciones reales del AMBA:
  `w_i = (1 / Error_i^2) / Suma(1 / Error_j^2)`

## 2. Filtro de Corrección de Sesgo con Decaimiento Exponencial (Kalman-like Nowcasting)
- Mide el sesgo en el instante actual (`Bias_0 = Temp_Real_Estaciones - Temp_BMA_0`) y corrige las próximas horas con decaimiento exponencial (`tau = 6 hs`):
  `T_pronosticada(t) = T_BMA(t) + Bias_0 * exp(-t / 6)`

## 3. Función Exponencial Hydro-Estimator (Tope Nuboso GOES) + Índice de Angström (Incendios)
- **Hydro-Estimator IR:** Cuando el tope nuboso infrarrojo cae por debajo de -45 °C, aplica un factor convectivo no lineal `1 + 0.18 * ((-45 - T_IR)/25)^1.4`.
- **Índice Forestal de Angström:** `I = (Humedad / 20) + ((27 - Temp) / 10) - 0.05 * Viento_kmh`. Valores `< 2.5` indican peligro crítico.
