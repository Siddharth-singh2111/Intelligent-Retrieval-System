# app/api/routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber

from app.utils.chunker import chunk_text
from app.utils.embedder import get_embeddings

router = APIRouter()

# Temporary in-memory store (use vector DB later)
vector_store = []

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        # Step 1: Extract text from PDF
        with pdfplumber.open(file.file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""

        if not text.strip():
            raise HTTPException(status_code=400, detail="No extractable text found in the PDF.")

        # Step 2: Chunk the text
        chunks = chunk_text(text)

        # Step 3: Embed the chunks
        embeddings = get_embeddings(chunks)

        # Step 4: Store in vector_store
        for chunk, embedding in zip(chunks, embeddings):
            vector_store.append({
                "chunk": chunk,
                "embedding": embedding,
                "source": file.filename
            })

        return {
            "message": "PDF processed and embedded successfully.",
            "total_chunks": len(chunks),
            "filename": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
