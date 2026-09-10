# EnerVision API

AI-powered renewable energy intelligence and decision support platform. Predicts solar radiation potential for a location and produces explainable, data-backed recommendations - built as an academic + portfolio project.

## Problem Statement
Renewable energy planning benefits from knowing not just current weather, but forecasted solar generation potential and what that means in practical terms. EnerVision combines live weather data, historical patterns, and machine learning to answer: "how much solar generation potential should I expect today, and what should I do with that information?"

## Objectives
- Ingest and clean historical solar/weather data
- Train and compare ML models for solar radiation forecasting
- Serve live, explainable predictions via a REST API
- Provide plain-language, data-backed recommendations (not a black box)

## Features
- Live weather lookup (Open-Meteo)
- Solar radiation forecasting (trained Random Forest model)
- Explainable recommendations based on historical percentile thresholds
- Full Swagger/OpenAPI documentation

## Architecture
```
EnerVision-API/
├── app/
│   ├── main.py, core/, api/, database/, models/, schemas/, services/, ml/, utils/
├── tests/
├── data/
├── notebooks/
├── docs/
├── models/  (saved ML artifacts)
```

## Technology Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **ML:** scikit-learn, pandas, numpy
- **External data:** Open-Meteo (live weather/forecast), NASA POWER (historical solar/meteorology)
- **Testing:** pytest, pytest-mock
- **Deployment:** Docker, Docker Compose

## Research Inspiration
- Danner, P. & de Meer, H. (2026). *Two-Stage Photovoltaic Forecasting: Separating Weather Prediction from Plant-Characteristics.* SMARTGREENS 2026. Informed the architectural separation between weather ingestion and the prediction model, and the emphasis on honest forecast-error evaluation.
- Metsch, T. & Hoban, A. (2025). *Breaking Barriers: From Black Box to Intent-Driven, User-Friendly Power Management.* SMARTGREENS 2025. A cross-domain (cloud/data-center power management) inspiration for the explainable, non-black-box design of the recommendation engine - not a renewable-energy methodology reproduced here.

## Project Structure
See Architecture above. Detailed docs in `docs/`.

## Installation
```bash
git clone https://github.com/official-darshan/EnerVision-API-AI-Powered-Renewable-Energy-Intelligence-Decision-Support-Platform.git
cd EnerVision-API-AI-Powered-Renewable-Energy-Intelligence-Decision-Support-Platform/EnerVision-API
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables
Copy `.env.example` to `.env` and fill in real values:
```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

## Running Locally
```bash
docker compose up -d db      # start PostgreSQL only
uvicorn app.main:app --reload
```

## Running with Docker (full stack)
```bash
docker compose up --build
```

## API Documentation
Interactive Swagger UI: `http://127.0.0.1:8000/docs`
Full endpoint reference: [`docs/api-design.md`](docs/api-design.md)

## ML Methodology
- **Baseline:** Linear Regression - MAE 0.85, RMSE 1.07, R² 0.72
- **Final model:** Random Forest (n_estimators=200, max_depth=8) - MAE 0.78, RMSE 1.03, R² 0.74
- Time-aware train/test split (no random shuffling) to avoid data leakage
- Features: humidity, temp_max, windspeed, day_of_year (selected based on EDA correlation analysis; temp_min excluded - correlation of 0.08 with target)
- Full details: [`notebooks/01_solar_eda.ipynb`](notebooks/01_solar_eda.ipynb)

## Results
Random Forest modestly outperformed the Linear Regression baseline on every metric (MAE improved ~8%, R² improved from 0.72 to 0.74). See ML Methodology above for full numbers.

## Testing
```bash
pytest -v
```
8 tests covering health check, input validation, and recommendation logic (mocked external API calls).

## Future Enhancements
- Wind energy analytics
- Energy demand forecasting
- Carbon intensity estimation (deferred - no reliable free API found for target region)
- Geocoding support (place name to coordinates, currently requires raw lat/lon)

## Limitations
- Solar-only scope; wind/demand/carbon intensity not yet implemented
- Model trained on 2 years of data for a single location (Mumbai); not yet validated for other regions
- No authentication/rate limiting implemented (not required at current scope)

## Research References
See Research Inspiration above.

## Author
Darshan - B.Sc. Data Science, KES Shroff College