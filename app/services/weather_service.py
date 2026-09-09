import httpx
from fastapi import HTTPException

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def get_current_weather(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,windspeed_10m,cloudcover,shortwave_radiation",
    }

    try:
        response = httpx.get(OPEN_METEO_URL, params=params, timeout=10.0)
        response.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Weather provider timed out")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Weather provider returned an error: {exc.response.status_code}",
        )

    data = response.json()
    current = data.get("current")

    if current is None:
        raise HTTPException(status_code=502, detail="Unexpected response from weather provider")

    return {
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "temperature_celsius": current["temperature_2m"],
        "windspeed_kmh": current["windspeed_10m"],
        "cloud_cover_percent": current["cloudcover"],
        "shortwave_radiation": current["shortwave_radiation"],
        "time": current["time"],
    }

def get_daily_forecast_features(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,relative_humidity_2m_mean,windspeed_10m_max",
        "timezone": "auto",
        "forecast_days": 1,
    }

    try:
        response = httpx.get(OPEN_METEO_URL, params=params, timeout=10.0)
        response.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Weather provider timed out")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Weather provider returned an error: {exc.response.status_code}",
        )

    data = response.json()
    daily = data.get("daily")

    if daily is None:
        raise HTTPException(status_code=502, detail="Unexpected response from weather provider")

    forecast_date = daily["time"][0]

    return {
        "temp_max": daily["temperature_2m_max"][0],
        "humidity": daily["relative_humidity_2m_mean"][0],
        "windspeed": daily["windspeed_10m_max"][0],
        "date": forecast_date,
    }