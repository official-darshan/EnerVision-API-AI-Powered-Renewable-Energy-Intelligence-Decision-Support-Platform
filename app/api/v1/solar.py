from fastapi import APIRouter, Query
from app.services.solar_service import predict_solar_radiation
from app.schemas.solar import SolarForecastResponse

router = APIRouter()


@router.get(
    "/solar/forecast",
    response_model=SolarForecastResponse,
    summary="Get solar radiation forecast",
    description="Predicts today's solar radiation potential for a location using live weather data and a trained Random Forest model.",
)
def read_solar_forecast(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
):
    return predict_solar_radiation(latitude=lat, longitude=lon)
