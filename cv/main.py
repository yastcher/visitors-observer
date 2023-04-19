import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup_event():
    pass


@app.get('/')
async def video_feed():
    pass


@app.get("/healthcheck")
def healthcheck():
    return 'Ok'


@app.on_event("shutdown")
def shutdown_event():
    pass
