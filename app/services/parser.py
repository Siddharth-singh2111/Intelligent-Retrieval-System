# app/services/parser.py
import requests
import pdfplumber
import os
from uuid import uuid4

def download_pdf_from_url(url: str, save_dir: str = "data") -> str:
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, f"{uuid4().hex}.pdf")
    
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
    
    return file_path

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def chunk_text(text: str, max_chunk_size: int = 500) -> list[str]:
    """
    Splits text into roughly 500-word chunks (you can tune this).
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_chunk_size):
        chunk = " ".join(words[i:i + max_chunk_size])
        chunks.append(chunk)
    return chunks
