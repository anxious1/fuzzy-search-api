from sqlalchemy.orm import Session
from app.models.search import SearchItem
from typing import List
from rapidfuzz import fuzz

def get_all_items(db: Session) -> List[SearchItem]:
    return db.query(SearchItem).all()

def fuzzy_search(db: Session, query: str, threshold: int = 60) -> List[SearchItem]:
    all_items = get_all_items(db)
    return [item for item in all_items if fuzz.partial_ratio(query.lower(), item.content.lower()) >= threshold]
