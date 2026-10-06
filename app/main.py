from fastapi import FastAPI

from app.config import settings

app = FastAPI(title = settings.app_name)


@app.get("/health")
def health():
    return {"status":"ok"}


@app.get("/info")
def info():
    return {
        "app_name": settings.app_name,
        "log_level": settings.log_level
    }