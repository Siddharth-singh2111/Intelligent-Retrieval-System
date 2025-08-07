from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts: list[str]) -> list[list[float]]:
    return model.encode(texts).tolist()

def embed_query(query: str) -> list[float]:
    return model.encode([query])[0].tolist()
