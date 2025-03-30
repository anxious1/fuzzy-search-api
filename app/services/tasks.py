from app.db.session import SessionLocal
from app.cruds.search import fuzzy_search
from app.models.search import SearchItem
from app.core.celery_app import celery

@celery.task
def run_fuzzy_search(query: str):
    db = SessionLocal()
    results = fuzzy_search(db, query)
    db.close()
    return [{"id": item.id, "content": item.content} for item in results]

if __name__ == "__main__":
    print("Этот файл не должен запускаться напрямую. Используй celery worker.")
