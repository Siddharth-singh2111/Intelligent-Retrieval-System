from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(title="LLM Query-Retrieval System")

@app.get("/")
def read_root():
    return {"message": "Intelligent Retrieval System API is running"}

app.include_router(router, prefix="/api/v1")
