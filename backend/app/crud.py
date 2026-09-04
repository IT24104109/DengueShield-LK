from typing import Optional

from sqlalchemy.orm import Session

from .models import Report, Area, SiteType, Urgency, ReportStatus
from .schemas import ReportCreate

VALID_TRANSITIONS: dict[ReportStatus, set[ReportStatus]] = {
    ReportStatus.REPORTED: {ReportStatus.VERIFIED},
    ReportStatus.VERIFIED: {ReportStatus.CLEARED},
    ReportStatus.CLEARED: set(),
}


def create_report(db: Session, payload: ReportCreate) -> Report:
    report = Report(
        area=payload.area,
        site_type=payload.site_type,
        description=payload.description,
        urgency=payload.urgency,
        reporter_contact=payload.reporter_contact,
        status=ReportStatus.REPORTED,
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


def list_reports(
    db: Session,
    area: Optional[Area] = None,
    site_type: Optional[SiteType] = None,
    status: Optional[ReportStatus] = None,
    urgency: Optional[Urgency] = None,
    q: Optional[str] = None,
) -> list[Report]:
    query = db.query(Report)
    if area is not None:
        query = query.filter(Report.area == area)
    if site_type is not None:
        query = query.filter(Report.site_type == site_type)
    if status is not None:
        query = query.filter(Report.status == status)
    if urgency is not None:
        query = query.filter(Report.urgency == urgency)
    if q:
        query = query.filter(Report.description.ilike(f"%{q}%"))
    return query.order_by(Report.created_at.desc()).all()


class InvalidTransitionError(Exception):
    pass


def update_status(db: Session, report_id: int, new_status: ReportStatus) -> Optional[Report]:
    report = db.query(Report).filter(Report.id == report_id).first()
    if report is None:
        return None
    if new_status != report.status and new_status not in VALID_TRANSITIONS[report.status]:
        raise InvalidTransitionError(
            f"Cannot move status from {report.status.value} to {new_status.value}"
        )
    report.status = new_status
    db.commit()
    db.refresh(report)
    return report
