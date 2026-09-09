from pydantic import BaseModel


class SolarForecastResponse(BaseModel):
    latitude: float
    longitude: float
    date: str
    predicted_solar_radiation: float
    inputs_used: dict