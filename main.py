from fastapi import FastAPI
from app.routers import analysis_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Social Analysis API!"}

# Include the analysis router
app.include_router(analysis_router)