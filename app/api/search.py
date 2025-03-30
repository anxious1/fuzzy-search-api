from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.search import SearchItemOut
from app.cruds.search import fuzzy_search
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/search/", response_model=List[SearchItemOut])
def search(query: str, db: Session = Depends(get_db)):
    return fuzzy_search(db, query)
