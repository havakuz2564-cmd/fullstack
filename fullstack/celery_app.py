import os

from celery import Celery

# Настройка Celery с использованием Redis в качестве брокера.
# URL можно переопределить через переменную окружения (например, для Docker Compose).
BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "tasks",
    broker=BROKER_URL,
    backend=BROKER_URL,
)
