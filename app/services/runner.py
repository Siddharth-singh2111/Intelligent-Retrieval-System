import json
import numpy as np
from app.utils.embedder import embed_query

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def semantic_search(query: str, file_id: str, top_k: int = 3):
    with open(f"data/{file_id}_chunks.json", "r") as f:
        chunks = json.load(f)

    with open(f"data/{file_id}_embeddings.json", "r") as f:
        embeddings = json.load(f)

    query_vec = embed_query(query)
    scored = [(cosine_similarity(query_vec, vec), chunk) for vec, chunk in zip(embeddings, chunks)]
    top_matches = sorted(scored, reverse=True)[:top_k]

    return [{"score": round(score, 3), "clause": chunk} for score, chunk in top_matches]
