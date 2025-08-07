from fastapi import APIRouter, UploadFile, File, HTTPException
import pdfplumber
from app.services.parser import parse_and_store
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        file_id = str(uuid.uuid4())
        with pdfplumber.open(file.file) as pdf:
            text = "".join(page.extract_text() or "" for page in pdf.pages)

        parse_and_store(text, file_id)
        return {"file_id": file_id, "message": "PDF processed and parsed."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
