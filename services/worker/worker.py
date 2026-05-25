import os
from redis import Redis
from rq import Worker, Queue

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

redis_conn = Redis(host=REDIS_HOST, port=6379)
queues = [Queue("crypto-jobs", connection=redis_conn)]

if __name__ == "__main__":
    worker = Worker(queues, connection=redis_conn)
    worker.work()