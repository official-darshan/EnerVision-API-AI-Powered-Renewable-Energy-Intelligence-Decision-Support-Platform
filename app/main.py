from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.v1 import health, weather, solar, recommendations
from app.core.config import APP_NAME, API_V1_PREFIX

app = FastAPI(title=APP_NAME)

app.include_router(health.router, prefix=API_V1_PREFIX)
app.include_router(weather.router, prefix=API_V1_PREFIX)
app.include_router(solar.router, prefix=API_V1_PREFIX)
app.include_router(recommendations.router, prefix=API_V1_PREFIX)


@app.exception_handler(Exception)
async def unhandled_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )