import re

def chunk_text(text: str, chunk_size: int = 5) -> list[str]:
    sentences = re.split(r'(?<=[.?!])\s+', text)
    return [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
