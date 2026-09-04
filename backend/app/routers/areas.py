from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..risk import get_all_areas_risk
from ..schemas import AreaRisk

router = APIRouter()


@router.get("/risk", response_model=list[AreaRisk])
def areas_risk(db: Session = Depends(get_db)):
    return get_all_areas_risk(db)
