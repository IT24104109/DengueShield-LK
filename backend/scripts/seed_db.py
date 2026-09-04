import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database import SessionLocal, Base, engine
from app.seed_data import seed

Base.metadata.create_all(bind=engine)
db = SessionLocal()
seed(db)
db.close()
print("Seed complete.")
