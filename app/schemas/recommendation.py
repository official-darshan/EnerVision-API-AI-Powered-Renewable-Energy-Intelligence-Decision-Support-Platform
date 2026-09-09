from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    latitude: float
    longitude: float
    date: str
    predicted_solar_radiation: float
    category: str
    recommendation: str
    reason: str