import datetime
import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from api import router

logging.basicConfig(level=logging.DEBUG if settings.debug else logging.INFO)


KWARGS_OPEN_API = {
    "title": "Visitor observer", "docs_url": "/docs", "redoc_url": "/redoc",
} if settings.debug else {"docs_url": None, "redoc_url": None}
app = FastAPI(**KWARGS_OPEN_API)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.from_apps)


@app.get("/")
async def root_endpoint(request: Request):
    return {
        "status": "OK",
        "timestamp": datetime.datetime.now(datetime.UTC),
        "swagger": "http://127.0.0.1:5555/docs",
    }


@app.get("/status")
async def health_check():
    return {"status": "OK", "timestamp": datetime.datetime.now(datetime.UTC)}
