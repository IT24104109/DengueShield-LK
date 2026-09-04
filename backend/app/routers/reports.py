from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db
from ..models import Area, SiteType, Urgency, ReportStatus

router = APIRouter()


@router.post("", response_model=schemas.ReportOut, status_code=201)
def create_report(payload: schemas.ReportCreate, db: Session = Depends(get_db)):
    return crud.create_report(db, payload)


@router.get("", response_model=list[schemas.ReportOut])
def list_reports(
    area: Optional[Area] = None,
    site_type: Optional[SiteType] = None,
    status: Optional[ReportStatus] = None,
    urgency: Optional[Urgency] = None,
    q: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return crud.list_reports(
        db, area=area, site_type=site_type, status=status, urgency=urgency, q=q
    )


@router.patch("/{report_id}/status", response_model=schemas.ReportOut)
def update_status(report_id: int, payload: schemas.StatusUpdate, db: Session = Depends(get_db)):
    try:
        report = crud.update_status(db, report_id, payload.status)
    except crud.InvalidTransitionError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
