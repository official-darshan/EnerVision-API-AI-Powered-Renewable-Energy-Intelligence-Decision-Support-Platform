import joblib
import pandas as pd
from datetime import datetime
from app.services.weather_service import get_daily_forecast_features

MODEL_PATH = "models/random_forest.pkl"
FEATURES = ["humidity", "temp_max", "windspeed", "day_of_year"]

_model = None


def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_solar_radiation(latitude: float, longitude: float) -> dict:
    weather = get_daily_forecast_features(latitude, longitude)

    forecast_date = datetime.strptime(weather["date"], "%Y-%m-%d")
    day_of_year = forecast_date.timetuple().tm_yday

    feature_row = pd.DataFrame([{
        "humidity": weather["humidity"],
        "temp_max": weather["temp_max"],
        "windspeed": weather["windspeed"],
        "day_of_year": day_of_year,
    }])[FEATURES]

    model = get_model()
    prediction = model.predict(feature_row)[0]

    return {
        "latitude": latitude,
        "longitude": longitude,
        "date": weather["date"],
        "predicted_solar_radiation": round(float(prediction), 4),
        "inputs_used": {
            "humidity": weather["humidity"],
            "temp_max": weather["temp_max"],
            "windspeed": weather["windspeed"],
            "day_of_year": day_of_year,
        },
    }