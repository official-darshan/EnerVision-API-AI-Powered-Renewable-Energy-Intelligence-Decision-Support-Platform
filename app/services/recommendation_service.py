import pandas as pd
from app.services.solar_service import predict_solar_radiation

HISTORICAL_DATA_PATH = "data/historical_solar_mumbai_clean.csv"

# Computed once at import time from actual historical distribution — not arbitrary
_historical_df = pd.read_csv(HISTORICAL_DATA_PATH)
LOW_THRESHOLD = _historical_df["solar_radiation"].quantile(0.33)
HIGH_THRESHOLD = _historical_df["solar_radiation"].quantile(0.67)


def categorize(value: float) -> tuple[str, str, str]:
    if value >= HIGH_THRESHOLD:
        return (
            "high",
            "High solar generation potential expected today.",
            f"Predicted radiation ({value:.2f} kWh/m²/day) is in the top third of this "
            f"location's historical range (above {HIGH_THRESHOLD:.2f}).",
        )
    elif value <= LOW_THRESHOLD:
        return (
            "low",
            "Low solar generation potential expected today — consider relying more on grid/stored power.",
            f"Predicted radiation ({value:.2f} kWh/m²/day) is in the bottom third of this "
            f"location's historical range (below {LOW_THRESHOLD:.2f}).",
        )
    else:
        return (
            "moderate",
            "Moderate solar generation potential expected today.",
            f"Predicted radiation ({value:.2f} kWh/m²/day) falls in the middle third of this "
            f"location's historical range ({LOW_THRESHOLD:.2f}–{HIGH_THRESHOLD:.2f}).",
        )


def generate_recommendation(latitude: float, longitude: float) -> dict:
    prediction = predict_solar_radiation(latitude, longitude)
    value = prediction["predicted_solar_radiation"]

    category, recommendation, reason = categorize(value)

    return {
        "latitude": latitude,
        "longitude": longitude,
        "date": prediction["date"],
        "predicted_solar_radiation": value,
        "category": category,
        "recommendation": recommendation,
        "reason": reason,
    }
