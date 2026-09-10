# EnerVision API

AI-powered renewable energy intelligence and decision support platform. Predicts solar radiation potential for a location and produces explainable, data-backed recommendations — built as an academic + portfolio project.

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

EnerVision-API/
├── app/
│ ├── main.py, core/, api/, database/, models/, schemas/, services/, ml/, utils/
├── tests/ ├── data/ ├── notebooks/ ├── docs/
├── models/ (saved ML artifacts)


## Technology Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **ML:** scikit-learn, pandas, numpy
- **External data:** Open-Meteo (live weather/forecast), NASA POWER (historical solar/meteorology)
- **Testing:** pytest, pytest-mock
- **Deployment:** Docker, Docker Compose

## Research Inspiration
- Danner, P. & de Meer, H. (2026). *Two-Stage Photovoltaic Forecasting: Separating Weather Prediction from Plant-Characteristics.* SMARTGREENS 2026. Informed the architectural separation between weather ingestion and the prediction model, and the emphasis on honest forecast-error evaluation.
- Metsch, T. & Hoban, A. (2025). *Breaking Barriers: From Black Box to Intent-Driven, User-Friendly Power Management.* SMARTGREENS 2025. A cross-domain (cloud/data-center power management) inspiration for the explainable, non-black-box design of the recommendation engine — not a renewable-energy methodology reproduced here.

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