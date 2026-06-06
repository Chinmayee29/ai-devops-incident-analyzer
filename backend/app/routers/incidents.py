from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.incident import IncidentCreate, IncidentUpdate

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get("/")
def get_incidents(db: Session = Depends(get_db)):
    incidents = db.query(Incident).all()
    return incidents

@router.get("/{incident_id}")
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        return {"error": "Incident not found"}

    return incident


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

@router.put("/{incident_id}")
def update_incident(
    incident_id: int,
    incident: IncidentUpdate,
    db: Session = Depends(get_db)
):
    db_incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not db_incident:
        return {"error": "Incident not found"}

    db_incident.status = incident.status

    db.commit()
    db.refresh(db_incident)

    return db_incident


@router.delete("/{incident_id}")
def delete_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):
    incident = (
        db.query(Incident)
        .filter(Incident.id == incident_id)
        .first()
    )

    if not incident:
        return {"error": "Incident not found"}

    db.delete(incident)
    db.commit()

    return {
        "message": f"Incident {incident_id} deleted successfully"
    }