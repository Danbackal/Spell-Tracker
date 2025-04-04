import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import spells

app = FastAPI()

origins = [
    'http://localhost',
    'localhost'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(spells.router)
