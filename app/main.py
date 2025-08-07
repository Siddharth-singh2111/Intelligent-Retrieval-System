from fastapi import FastAPI
from app.api.routes import router
from app.api.query import router as query_router

app = FastAPI(title="LLM Queries-Retrieval System")

@app.get("/")
def read_root():
    return {"message": "Intelligent Retrieval System API is running"}

app.include_router(router, prefix="/api/v1")
app.include_router(query_router, prefix="/api/v1")
