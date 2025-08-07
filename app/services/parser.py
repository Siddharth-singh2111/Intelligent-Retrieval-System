from app.utils.chunker import chunk_text
from app.utils.embedder import get_embeddings
import json
import os

def parse_and_store(file_text: str, file_id: str):
    chunks = chunk_text(file_text)
    embeddings = get_embeddings(chunks)

    os.makedirs("data", exist_ok=True)
    with open(f"data/{file_id}_chunks.json", "w") as f:
        json.dump(chunks, f)

    with open(f"data/{file_id}_embeddings.json", "w") as f:
        json.dump(embeddings, f)
