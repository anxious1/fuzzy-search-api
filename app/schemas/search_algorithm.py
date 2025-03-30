from pydantic import BaseModel
from typing import List

class SearchAlgorithmRequest(BaseModel):
    query: str
    algorithm: str  # 'levenshtein' или 'ngram'
    corpus_id: int

class SearchAlgorithmResponse(BaseModel):
    results: List[str]
    duration: float
