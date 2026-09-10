from fastapi import APIRouter, Query
from app.services.weather_service import get_current_weather
from app.schemas.weather import WeatherResponse

router = APIRouter()


@router.get(
    "/weather",
    response_model=WeatherResponse,
    summary="Get current weather",
    description="Fetches current live weather conditions (temperature, wind, cloud cover, solar radiation) for a given latitude/longitude using the Open-Meteo API.",
)
def read_weather(
    
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
):
    return get_current_weather(latitude=lat, longitude=lon)