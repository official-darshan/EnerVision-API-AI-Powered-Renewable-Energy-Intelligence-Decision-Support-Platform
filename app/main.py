from fastapi import FastAPI

app = FastAPI(title="EnerVision API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
