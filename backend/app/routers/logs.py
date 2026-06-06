from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_log(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Log uploaded successfully",
        "filename": file.filename
    }

@router.get("/analyze/{filename}")
def analyze_log(filename: str):

    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.readlines()

    error_count = sum(
        1 for line in content
        if "error" in line.lower()
    )

    warning_count = sum(
        1 for line in content
        if "warning" in line.lower()
    )

    return {
        "filename": filename,
        "total_lines": len(content),
        "error_count": error_count,
        "warning_count": warning_count
    }