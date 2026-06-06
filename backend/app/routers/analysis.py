from fastapi import APIRouter
from app.services.log_analyzer import analyze_log

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

@router.get("/")
def analyze():
    return analyze_log("dummy.log")