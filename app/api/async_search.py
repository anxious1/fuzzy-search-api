from fastapi import APIRouter
from app.services.tasks import run_fuzzy_search

router = APIRouter()

@router.post("/search/async/")
def start_async_search(query: str):
    task = run_fuzzy_search.delay(query)
    return {"task_id": task.id}

@router.get("/search/result/{task_id}")
def get_async_result(task_id: str):
    result = run_fuzzy_search.AsyncResult(task_id)
    if result.ready():
        return result.result
    return {"status": "processing"}
