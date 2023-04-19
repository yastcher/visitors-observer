import datetime
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import config
from api.endpoints import router

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.from_apps)


@app.on_event("startup")
async def startup_event():
    pass


@app.get("/")
async def healthcheck():
    return {
        "status": "OK",
        "timestamp": datetime.datetime.utcnow(),
        "swagger": "http://127.0.0.1:5555/docs",
    }


@app.on_event("shutdown")
def shutdown_event():
    pass
