from fastapi import FastAPI

app = FastAPI(
    title="AI DevOps Incident Analyzer",
    description="Backend API for AI-powered DevOps incident analysis",
    version="1.0.0"
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