"""Sample data loader.

STUB — the Design Lead's branch replaces this file with the real 18-report
seed table (locked risk distribution: 4 Low / 3 Medium / 1 High areas).
This placeholder exists only so the backend runs standalone before that
branch is merged.
"""

from sqlalchemy.orm import Session

from .models import Report


def seed(db: Session) -> None:
    if db.query(Report).count() > 0:
        return
    # No rows yet — replaced by the Design Lead's branch.
    pass
