from fastapi import APIRouter, Query
from app.services.recommendation_service import generate_recommendation
from app.schemas.recommendation import RecommendationResponse

router = APIRouter()


@router.get("/recommendations/forecast", response_model=RecommendationResponse)
def read_recommendation(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
):
    return generate_recommendation(latitude=lat, longitude=lon)