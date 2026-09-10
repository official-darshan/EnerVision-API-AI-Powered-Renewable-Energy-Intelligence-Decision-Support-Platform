from fastapi import APIRouter, Query
from app.services.recommendation_service import generate_recommendation
from app.schemas.recommendation import RecommendationResponse

router = APIRouter()


@router.get(
    "/recommendations/forecast",
    response_model=RecommendationResponse,
    summary="Get an explainable solar recommendation",
    description="Combines the solar radiation forecast with historical percentile thresholds to produce a plain-language recommendation with a stated reason.",
)
def read_recommendation(
    lat: float = Query(..., ge=-90, le=90, description="Latitude"),
    lon: float = Query(..., ge=-180, le=180, description="Longitude"),
):
    return generate_recommendation(latitude=lat, longitude=lon)