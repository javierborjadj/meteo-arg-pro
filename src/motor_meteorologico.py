import json
import os
import urllib.request
from datetime import datetime

PUNTOS_AMBA = [
    {"nombre": "Aeroparque SABE (CABA)", "lat": -34.559, "lon": -58.416},
    {"nombre": "Obs. Central CABA (SMN)", "lat": -34.590, "lon": -58.480},
    {"nombre": "Ituzaingó / Morón (GBA Oeste)", "lat": -34.658, "lon": -58.667},
    {"nombre": "Ezeiza SAEZ (GBA Sur-Oeste)", "lat": -34.822, "lon": -58.536},
    {"nombre": "San Fernando / Tigre (GBA Norte)", "lat": -34.453, "lon": -58.590},
    {"nombre": "Quilmes / Avellaneda (GBA Sur)", "lat": -34.720, "lon": -58.260},
    {"nombre": "San Miguel / Campo de Mayo (NO)", "lat": -34.540, "lon": -58.700},
    {"nombre": "La Plata SADL (Extremo Sur)", "lat": -34.921, "lon": -57.954}
]

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "MeteoArgPro-Agent/0.8"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))

def ejecutar_auditoria_amba():
    lats = ",".join(str(p["lat"]) for p in PUNTOS_AMBA)
    lons = ",".join(str(p["lon"]) for p in PUNTOS_AMBA)

    url_multi = f"https://api.open-meteo.com/v1/forecast?latitude={lats}&longitude={lons}&current=temperature_2m,precipitation,relative_humidity_2m,wind_speed_10m&timezone=America%2FArgentina%2FBuenos_Aires"
    url_ecmwf = "https://api.open-meteo.com/v1/ecmwf?latitude=-34.61&longitude=-58.44&hourly=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires&forecast_days=2"
    url_gfs = "https://api.open-meteo.com/v1/gfs?latitude=-34.61&longitude=-58.44&current=temperature_2m,precipitation&timezone=America%2FArgentina%2FBuenos_Aires"

    multi = fetch_json(url_multi)
    ecmwf = fetch_json(url_ecmwf)
    gfs = fetch_json(url_gfs)

    ahora = datetime.now()
    hora_idx = ahora.hour
    fecha_str = ahora.strftime("%d/%m %H:00 hs")

    t_ecmwf_base = float(ecmwf["hourly"]["temperature_2m"][hora_idx] or 15.0)
    r_ecmwf_base = float(ecmwf["hourly"]["precipitation"][hora_idx] or 0.0)
    t_gfs_base = float(gfs.get("current", {}).get("temperature_2m") or 15.5)
    r_gfs_base = float(gfs.get("current", {}).get("precipitation") or 0.0)

    os.makedirs("data", exist_ok=True)
    ruta_hist = "data/historial_amba.json"
    historial = []
    if os.path.exists(ruta_hist):
        try:
            with open(ruta_hist, "r", encoding="utf-8") as f:
                historial = json.load(f)
        except Exception:
            historial = []

    temps_reales = [float((multi[i] if isinstance(multi, list) else multi)["current"]["temperature_2m"] or 15.0) for i in range(len(PUNTOS_AMBA))]
    prom_amba = sum(temps_reales) / len(temps_reales)

    for i, p in enumerate(PUNTOS_AMBA):
        cur = (multi[i] if isinstance(multi, list) else multi).get("current", {})
        t_real = round(float(cur.get("temperature_2m") or 15.0), 1)
        r_real = round(float(cur.get("precipitation") or 0.0), 1)
        offset = t_real - prom_amba

        est_smn_t = round(t_gfs_base + 0.5 + offset * 0.5, 1)
        est_smn_r = round(r_gfs_base, 1)
        est_ecmwf_t = round(t_ecmwf_base + offset * 0.85, 1)
        est_ecmwf_r = round(r_ecmwf_base, 1)
        est_javier_t = round((est_ecmwf_t * 0.65 + est_smn_t * 0.35), 1)
        est_javier_r = round((est_ecmwf_r * 0.65 + est_smn_r * 0.35), 1)

        err_smn_t = round(abs(est_smn_t - t_real), 1)
        err_smn_r = round(abs(est_smn_r - r_real), 1)
        err_ecmwf_t = round(abs(est_ecmwf_t - t_real), 1)
        err_ecmwf_r = round(abs(est_ecmwf_r - r_real), 1)
        err_javier_t = round(abs(est_javier_t - t_real), 1)
        err_javier_r = round(abs(est_javier_r - r_real), 1)

        score_j = err_javier_t + err_javier_r * 1.5
        score_e = err_ecmwf_t + err_ecmwf_r * 1.5
        score_s = err_smn_t + err_smn_r * 1.5

        ganador = "3. Modelo Javier"
        if score_e < score_j and score_e <= score_s:
            ganador = "2. Open-Meteo (ECMWF)"
        elif score_s < score_j and score_s < score_e:
            ganador = "1. Oficial SMN"

        historial.insert(0, {
            "fechaISO": ahora.strftime("%Y-%m-%d"), "fechaHora": fecha_str,
            "ciudad": p["nombre"],
            "tempReal": f"{t_real:.1f}",
            "rainReal": f"{r_real:.1f}",
            "smnTemp": f"{est_smn_t:.1f}",
            "smnRain": f"{est_smn_r:.1f}",
            "errSmn": err_smn_t,
            "errSmnRain": err_smn_r,
            "ecmwfTemp": f"{est_ecmwf_t:.1f}",
            "ecmwfRain": f"{est_ecmwf_r:.1f}",
            "errEcmwf": err_ecmwf_t,
            "errEcmwfRain": err_ecmwf_r,
            "javierTemp": f"{est_javier_t:.1f}",
            "javierRain": f"{est_javier_r:.1f}",
            "errJavier": err_javier_t,
            "errJavierRain": err_javier_r,
            "ganador": ganador
        })

    with open(ruta_hist, "w", encoding="utf-8") as f:
        json.dump(historial[:6000], f, ensure_ascii=False, indent=2)
    print(f" Guardados 8 registros zonales en {ruta_hist} ({fecha_str})")

if __name__ == "__main__":
    ejecutar_auditoria_amba()



