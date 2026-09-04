from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from .models import Report, Area, ReportStatus

RISK_WINDOW_DAYS = 30


def compute_risk_level(active_count: int) -> str:
    if active_count >= 5:
        return "High"
    if active_count >= 2:
        return "Medium"
    return "Low"


def get_area_risk(db: Session, area: Area, now: Optional[datetime] = None) -> dict:
    now = now or datetime.utcnow()
    cutoff = now - timedelta(days=RISK_WINDOW_DAYS)
    count = (
        db.query(func.count(Report.id))
        .filter(Report.area == area)
        .filter(Report.status != ReportStatus.CLEARED)
        .filter(Report.created_at >= cutoff)
        .scalar()
    ) or 0
    return {
        "area": area,
        "active_report_count": count,
        "risk_level": compute_risk_level(count),
    }


def get_all_areas_risk(db: Session, now: Optional[datetime] = None) -> list[dict]:
    return [get_area_risk(db, area, now) for area in Area]
