from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from redis import Redis
from rq import Queue
import requests
import os

app = FastAPI(title="Crypto Price Tracking API")

Instrumentator().instrument(app).expose(app)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
redis_conn = Redis(host=REDIS_HOST, port=6379)
queue = Queue("crypto-jobs", connection=redis_conn)

def fetch_crypto_price(coin: str):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin, "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

@app.get("/")
def root():
    return {"message": "Crypto API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/price/{coin}")
def get_price(coin: str):
    return fetch_crypto_price(coin)

@app.post("/track/{coin}")
def track_coin(coin: str):
    job = queue.enqueue("worker.fetch_and_store_price", coin)
    return {
        "message": "Tracking job added",
        "coin": coin,
        "job_id": job.id
    }