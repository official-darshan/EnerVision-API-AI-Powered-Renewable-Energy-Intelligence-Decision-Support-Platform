from fastapi import APIRouter, Query
from app.services.solar_service import predict_solar_radiation
from app.schemas.solar import SolarForecastResponse

router = APIRouter()


@router.get("/solar/forecast", response_model=SolarForecastResponse)
def read_solar_forecast(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
):
    return predict_solar_radiation(latitude=lat, longitude=lon)
