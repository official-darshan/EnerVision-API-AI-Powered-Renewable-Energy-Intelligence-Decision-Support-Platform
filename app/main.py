from fastapi import FastAPI
from app.api.v1 import health
from app.core.config import APP_NAME, API_V1_PREFIX

app = FastAPI(title=APP_NAME)

app.include_router(health.router, prefix=API_V1_PREFIX)