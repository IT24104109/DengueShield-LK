import enum

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import Enum as SAEnum
from sqlalchemy.sql import func

from .database import Base


class Area(str, enum.Enum):
    WELLAWATTE = "Wellawatte"
    DEHIWALA = "Dehiwala"
    KOTTE = "Kotte"
    MAHARAGAMA = "Maharagama"
    KADUWELA = "Kaduwela"
    NEGOMBO = "Negombo"
    KANDY_TOWN = "Kandy Town"
    GALLE_FORT = "Galle Fort"


class SiteType(str, enum.Enum):
    BLOCKED_DRAIN = "Blocked Drain"
    DISCARDED_TYRE = "Discarded Tyre"
    OPEN_CONTAINER = "Open Container"
    WATER_TANK = "Water Tank"
    CONSTRUCTION_SITE = "Construction Site"
    OTHER = "Other"


class Urgency(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class ReportStatus(str, enum.Enum):
    REPORTED = "Reported"
    VERIFIED = "Verified"
    CLEARED = "Cleared"


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    area = Column(SAEnum(Area), nullable=False, index=True)
    site_type = Column(SAEnum(SiteType), nullable=False, index=True)
    description = Column(Text, nullable=False)
    urgency = Column(SAEnum(Urgency), nullable=False, default=Urgency.MEDIUM, index=True)
    reporter_contact = Column(String(120), nullable=True)
    status = Column(SAEnum(ReportStatus), nullable=False, default=ReportStatus.REPORTED, index=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now(), index=True)
