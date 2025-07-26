from app.services.parser import download_pdf_from_url, extract_text_from_pdf, chunk_text

async def process_documents(doc_url: str, questions: list[str]):
    file_path = download_pdf_from_url(doc_url)
    raw_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(raw_text)

    # For now, just return a sample preview of chunks
    return {
        "chunk_count": len(chunks),
        "sample_chunk": chunks[0] if chunks else "No text found",
        "questions": questions
    }
