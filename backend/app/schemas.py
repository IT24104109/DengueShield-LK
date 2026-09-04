import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from .models import Area, SiteType, Urgency, ReportStatus

_PHONE_RE = re.compile(r"^\+?\d{7,15}$")
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class ReportCreate(BaseModel):
    area: Area
    site_type: SiteType
    description: str = Field(..., min_length=15)
    urgency: Urgency = Urgency.MEDIUM
    reporter_contact: Optional[str] = None

    @field_validator("reporter_contact")
    @classmethod
    def validate_contact(cls, v):
        if v is None or v.strip() == "":
            return None
        v = v.strip()
        if not (_PHONE_RE.match(v) or _EMAIL_RE.match(v)):
            raise ValueError("Contact must be a valid phone number or email address")
        return v


class ReportOut(BaseModel):
    id: int
    area: Area
    site_type: SiteType
    description: str
    urgency: Urgency
    reporter_contact: Optional[str]
    status: ReportStatus
    created_at: datetime

    class Config:
        from_attributes = True


class StatusUpdate(BaseModel):
    status: ReportStatus


class AreaRisk(BaseModel):
    area: Area
    active_report_count: int
    risk_level: str


class SuggestRequest(BaseModel):
    description: str = Field(..., min_length=3)


class SuggestResponse(BaseModel):
    suggested_site_type: SiteType
    source: str
