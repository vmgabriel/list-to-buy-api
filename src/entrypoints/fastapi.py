"""Fast Api All Entrypoints"""

# Libraries
from fastapi import FastAPI

# Modules
from src.config import config


app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}
