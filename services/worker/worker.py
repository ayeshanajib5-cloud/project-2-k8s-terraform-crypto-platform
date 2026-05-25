import os
import time
import requests
import psycopg2
from redis import Redis
from rq import Worker, Queue

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "cryptodb")
DB_USER = os.getenv("DB_USER", "crypto_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "crypto_pass")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def create_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            coin VARCHAR(50),
            price_usd NUMERIC,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def fetch_and_store_price(coin: str):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    price = data.get(coin, {}).get("usd")

    if price is None:
        return {"error": "Coin price not found", "coin": coin}

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO crypto_prices (coin, price_usd) VALUES (%s, %s)",
        (coin, price)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {
        "coin": coin,
        "price_usd": price,
        "status": "stored"
    }


if __name__ == "__main__":
    time.sleep(5)
    create_table()

    redis_conn = Redis(host=REDIS_HOST, port=6379)
    queues = [Queue("crypto-jobs", connection=redis_conn)]

    worker = Worker(queues, connection=redis_conn)
    worker.work()