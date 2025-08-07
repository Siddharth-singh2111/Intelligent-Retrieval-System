from fastapi import APIRouter, HTTPException, Query
from app.services.runner import semantic_search

router = APIRouter()

@router.get("/query")
def query_pdf(file_id: str = Query(...), query: str = Query(...)):
    try:
        result = semantic_search(query, file_id)
        return {"matches": result}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found or not yet parsed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
