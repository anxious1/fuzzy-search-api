from celery import Celery

celery = Celery(
    "fuzzy_search",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.task_routes = {
    "app.services.tasks.*": {"queue": "search"}
}
