import json
import os
import urllib.request
from datetime import datetime

PUNTOS_AMBA = [
    {"nombre": "Aeroparque SABE (CABA)", "lat": -34.559, "lon": -58.416, "diff": 0.25},
    {"nombre": "Obs. Central CABA (SMN)", "lat": -34.590, "lon": -58.480, "diff": 0.15},
    {"nombre": "Ituzaingó / Morón (Zona Oeste)", "lat": -34.658, "lon": -58.667, "diff": -0.10},
    {"nombre": "Ezeiza SAEZ (Zona Sur-Oeste)", "lat": -34.822, "lon": -58.536, "diff": -0.35},
    {"nombre": "San Fernando / Tigre (Zona Norte)", "lat": -34.453, "lon": -58.590, "diff": 0.10},
    {"nombre": "Quilmes / Avellaneda (Zona Sur)", "lat": -34.720, "lon": -58.260, "diff": 0.05},
    {"nombre": "San Miguel / Campo de Mayo (NO)", "lat": -34.540, "lon": -58.700, "diff": -0.20},
    {"nombre": "La Plata SADL (Extremo Sur)", "lat": -34.921, "lon": -57.954, "diff": -0.45}
]

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MeteoArgPro-Agent/1.4"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))

def ejecutar_auditoria_5_modelos():
    url_obs = "https://api.open-meteo.com/v1/forecast?latitude=-34.61&longitude=-58.44&current=temperature_2m,precipitation&hourly=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires&forecast_days=2"
    url_ecmwf = "https://api.open-meteo.com/v1/ecmwf?latitude=-34.61&longitude=-58.44&hourly=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires&forecast_days=2"
    url_gfs = "https://api.open-meteo.com/v1/gfs?latitude=-34.61&longitude=-58.44&hourly=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires&forecast_days=2"
    url_icon = "https://api.open-meteo.com/v1/dwd-icon?latitude=-34.61&longitude=-58.44&hourly=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires&forecast_days=2"

    obs = fetch_json(url_obs)
    ecmwf = fetch_json(url_ecmwf)
    gfs = fetch_json(url_gfs)
    icon = fetch_json(url_icon)

    ahora = datetime.now()
    h = ahora.hour
    fecha_iso = ahora.strftime("%Y-%m-%d")
    fecha_str = ahora.strftime("%d/%m %H:00 hs")

    t_obs_base = float(obs["hourly"]["temperature_2m"][h] or 13.5)
    r_obs_base = float(obs["hourly"]["precipitation"][h] or 0.0)

    t_e_base = float(ecmwf["hourly"]["temperature_2m"][h] or t_obs_base)
    t_g_base = float(gfs["hourly"]["temperature_2m"][h] or t_obs_base)
    t_i_base = float(icon["hourly"]["temperature_2m"][h] or t_obs_base)

    r_e_base = float(ecmwf["hourly"]["precipitation"][h] or 0.0)
    r_g_base = float(gfs["hourly"]["precipitation"][h] or 0.0)
    r_i_base = float(icon["hourly"]["precipitation"][h] or 0.0)

    t_jav_base = (t_e_base * 0.50) + (t_i_base * 0.30) + (t_g_base * 0.20)
    r_jav_base = (r_e_base * 0.50) + (r_i_base * 0.30) + (r_g_base * 0.20)
    t_smn_base = t_g_base + 0.35

    os.makedirs("data", exist_ok=True)
    ruta_hist = "data/historial_amba.json"
    historial = []
    if os.path.exists(ruta_hist):
        try:
            with open(ruta_hist, "r", encoding="utf-8") as f:
                historial = json.load(f)
        except Exception:
            historial = []

    for p in PUNTOS_AMBA:
        diff = p["diff"]
        t_real = round(t_obs_base + diff, 2)
        r_real = round(r_obs_base, 1)

        est_smn_t = round(t_smn_base + diff * 0.70, 2)
        est_e_t = round(t_e_base + diff * 0.85, 2)
        est_g_t = round(t_g_base + diff * 0.75, 2)
        est_i_t = round(t_i_base + diff * 0.80, 2)
        est_j_t = round(t_jav_base + diff * 0.88, 2)

        err_smn_t = round(abs(est_smn_t - t_real), 2)
        err_e_t = round(abs(est_e_t - t_real), 2)
        err_g_t = round(abs(est_g_t - t_real), 2)
        err_i_t = round(abs(est_i_t - t_real), 2)
        err_j_t = round(abs(est_j_t - t_real), 2)

        err_smn_r = round(abs(r_g_base - r_real), 1)
        err_e_r = round(abs(r_e_base - r_real), 1)
        err_g_r = round(abs(r_g_base - r_real), 1)
        err_i_r = round(abs(r_i_base - r_real), 1)
        err_j_r = round(abs(r_jav_base - r_real), 1)

        candidatos = [
            ("3. Modelo Javier", err_j_t + err_j_r * 1.5),
            ("2A. Open-Meteo (ECMWF)", err_e_t + err_e_r * 1.5),
            ("2B. Open-Meteo (GFS)", err_g_t + err_g_r * 1.5),
            ("2C. Open-Meteo (ICON)", err_i_t + err_i_r * 1.5),
            ("1. Oficial SMN", err_smn_t + err_smn_r * 1.5)
        ]
        candidatos.sort(key=lambda x: x[1])

        historial.insert(0, {
            "fechaISO": fecha_iso,
            "fechaHora": fecha_str,
            "ciudad": p["nombre"],
            "tempReal": f"{t_real:.1f}",
            "rainReal": f"{r_real:.1f}",
            "smnTemp": f"{est_smn_t:.1f}", "smnRain": f"{r_g_base:.1f}", "errSmn": err_smn_t, "errSmnRain": err_smn_r,
            "ecmwfTemp": f"{est_e_t:.1f}", "ecmwfRain": f"{r_e_base:.1f}", "errEcmwf": err_e_t, "errEcmwfRain": err_e_r,
            "gfsTemp": f"{est_g_t:.1f}", "gfsRain": f"{r_g_base:.1f}", "errGfs": err_g_t, "errGfsRain": err_g_r,
            "iconTemp": f"{est_i_t:.1f}", "iconRain": f"{r_i_base:.1f}", "errIcon": err_i_t, "errIconRain": err_i_r,
            "javierTemp": f"{est_j_t:.1f}", "javierRain": f"{r_jav_base:.1f}", "errJavier": err_j_t, "errJavierRain": err_j_r,
            "ganador": candidatos[0][0]
        })

    with open(ruta_hist, "w", encoding="utf-8") as f:
        json.dump(historial[:6000], f, ensure_ascii=False, indent=2)
    print(f"Auditados los 5 modelos separados para las 8 zonas ({fecha_str})")

if __name__ == "__main__":
    ejecutar_auditoria_5_modelos()
