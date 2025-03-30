from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.corpus import CorpusCreate, CorpusOut
from app.cruds import corpus as corpus_crud
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload_corpus", response_model=CorpusOut)
def upload_corpus(corpus: CorpusCreate, db: Session = Depends(get_db)):
    return corpus_crud.create_corpus(db, corpus)

@router.get("/corpuses", response_model=List[CorpusOut])
def get_corpuses(db: Session = Depends(get_db)):
    return corpus_crud.get_all_corpuses(db)
