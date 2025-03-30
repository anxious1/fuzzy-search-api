import time
from typing import List, Tuple
from difflib import SequenceMatcher
from rapidfuzz.distance import Levenshtein

# Вернёт (результаты, время_в_секундах)
def search_levenshtein(query: str, corpus: str, threshold: int = 0.6) -> Tuple[List[str], float]:
    start = time.time()
    results = []
    for line in corpus.splitlines():
        ratio = Levenshtein.normalized_similarity(query.lower(), line.lower())
        if ratio >= threshold:
            results.append(line)
    duration = time.time() - start
    return results, duration


def generate_ngrams(text: str, n: int = 3) -> List[str]:
    text = text.lower()
    return [text[i:i+n] for i in range(len(text)-n+1)]


def search_ngrams(query: str, corpus: str, threshold: float = 0.5) -> Tuple[List[str], float]:
    start = time.time()
    results = []
    query_ngrams = set(generate_ngrams(query))
    for line in corpus.splitlines():
        line_ngrams = set(generate_ngrams(line))
        overlap = len(query_ngrams & line_ngrams) / max(1, len(query_ngrams | line_ngrams))
        if overlap >= threshold:
            results.append(line)
    duration = time.time() - start
    return results, duration
