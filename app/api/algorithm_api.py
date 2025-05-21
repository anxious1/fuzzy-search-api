from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.cruds.corpus import get_corpus_by_id
from app.schemas.search_algorithm import SearchAlgorithmRequest, SearchAlgorithmResponse
from app.services import algorithms

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/search_algorithm", response_model=SearchAlgorithmResponse)
def search_algorithm(payload: SearchAlgorithmRequest, db: Session = Depends(get_db)):
    corpus = get_corpus_by_id(db, payload.corpus_id)
    if not corpus:
        raise HTTPException(status_code=404, detail="Корпус не найден")

    if payload.algorithm == "levenshtein":
        results, duration = algorithms.search_levenshtein(payload.query, corpus.content)
    elif payload.algorithm == "ngram":
        results, duration = algorithms.search_ngrams(payload.query, corpus.content)
    else:
        raise HTTPException(status_code=400, detail="Неизвестный алгоритм")

    return {"results": results, "duration": duration}
