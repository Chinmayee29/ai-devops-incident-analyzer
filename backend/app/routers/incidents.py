from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get("/")
def get_incidents(db: Session = Depends(get_db)):
    incidents = db.query(Incident).all()
    return incidents

@router.post("/")
def create_incident(
    incident: IncidentCreate,
    db: Session = Depends(get_db)
):
    db_incident = Incident(
        title=incident.title,
        description=incident.description,
        severity=incident.severity
    )

    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)

    return db_incident