from pydantic import BaseModel


class WeatherResponse(BaseModel):
    latitude: float
    longitude: float
    temperature_celsius: float
    windspeed_kmh: float
    cloud_cover_percent: float
    shortwave_radiation: float
    time: str