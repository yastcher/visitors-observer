import datetime
import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import config
from api import router

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


app = FastAPI(
    **config.KWARGS_OPEN_API,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.from_apps)


@app.get("/")
async def healthcheck(request: Request):
    return {
        "status": "OK",
        "timestamp": datetime.datetime.utcnow(),
        "swagger": "http://127.0.0.1:5555/docs",
    }
