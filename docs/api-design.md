# EnerVision API — Endpoint Documentation

All endpoints are prefixed with `/api/v1`.

## GET /api/v1/health
Health check — confirms the API is running.

**Parameters:** none

**Example response (200):**
```json
{"status": "ok"}
```

---

## GET /api/v1/weather
Fetches current live weather for a location via Open-Meteo.

**Parameters:**
| Name | Type | Required | Description |
|---|---|---|---|
| lat | float | yes | Latitude (-90 to 90) |
| lon | float | yes | Longitude (-180 to 180) |

**Example request:** `/api/v1/weather?lat=19.0760&lon=72.8777`

**Example response (200):**
```json
{
  "latitude": 19.086115,
  "longitude": 72.85291,
  "temperature_celsius": 29.4,
  "windspeed_kmh": 13.2,
  "cloud_cover_percent": 20,
  "shortwave_radiation": 822,
  "time": "2026-09-09T08:30"
}
```

**Error responses:** `422` invalid lat/lon, `502` upstream provider error, `504` upstream timeout.

---

## GET /api/v1/solar/forecast
Predicts today's solar radiation using a trained Random Forest model and live daily forecast weather.

**Parameters:** same as `/weather` (lat, lon)

**Example response (200):**
```json
{
  "latitude": 19.076,
  "longitude": 72.8777,
  "date": "2026-09-10",
  "predicted_solar_radiation": 5.0257,
  "inputs_used": {
    "humidity": 85,
    "temp_max": 29,
    "windspeed": 11.5,
    "day_of_year": 253
  }
}
```

**Error responses:** `422` invalid lat/lon, `502`/`504` upstream weather provider issues, `503` if the trained model file is unavailable.

---

## GET /api/v1/recommendations/forecast
Produces an explainable recommendation based on the solar forecast and historical percentile thresholds.

**Parameters:** same as `/weather` (lat, lon)

**Example response (200):**
```json
{
  "latitude": 19.076,
  "longitude": 72.8777,
  "date": "2026-09-10",
  "predicted_solar_radiation": 5.0257,
  "category": "moderate",
  "recommendation": "Moderate solar generation potential expected today.",
  "reason": "Predicted radiation (5.03 kWh/m²/day) falls in the middle third of this location's historical range (4.41–5.74)."
}
```

**Error responses:** same as `/solar/forecast`, since it depends on the same prediction pipeline.
