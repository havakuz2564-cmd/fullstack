from celery import Celery

# Настройка Celery с использованием Redis в качестве брокера
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)