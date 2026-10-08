import logging
from fastapi import FastAPI

from app.config import settings

app = FastAPI(title = settings.app_name)

from app.webhook import router as webhook_router

logging.basicConfig(level=settings.log_level, format="%(levelname)s: %(message)s")




app.include_router(webhook_router)


@app.get("/health")
def health():
    return {"status":"ok"}


@app.get("/info")
def info():
    return {
        "app_name": settings.app_name,
        "log_level": settings.log_level
    }