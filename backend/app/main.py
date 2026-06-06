from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for AI-powered DevOps incident analysis"
)


@app.get("/")
def root(): 
    return {
        "message": "AI DevOps Incident Analyzer API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/info")
def info():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION
    }