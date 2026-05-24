from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import requests

app = FastAPI(title="Crypto Price Tracking API")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "Crypto API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/price/{coin}")
def get_price(coin: str):

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    return response.json()