from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


@router.get("/")
def get_stats(db: Session = Depends(get_db)):

    total_incidents = db.query(Incident).count()

    open_incidents = (
        db.query(Incident)
        .filter(Incident.status == "open")
        .count()
    )

    resolved_incidents = (
        db.query(Incident)
        .filter(Incident.status == "resolved")
        .count()
    )

    high_severity_incidents = (
        db.query(Incident)
        .filter(Incident.severity == "high")
        .count()
    )

    return {
        "total_incidents": total_incidents,
        "open_incidents": open_incidents,
        "resolved_incidents": resolved_incidents,
        "high_severity_incidents": high_severity_incidents
    }