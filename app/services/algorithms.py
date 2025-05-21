import time
def levenshtein_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      
                dp[i][j - 1] + 1,      
                dp[i - 1][j - 1] + cost  
            )

    return dp[len1][len2]

def generate_ngrams(text, n=3):
    text = text.lower()
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def search_ngrams(query, corpus, threshold=0.5):
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

