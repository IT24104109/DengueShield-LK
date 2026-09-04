from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CORS_ORIGINS
from .database import Base, engine
from .routers import reports, areas, suggest

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DengueShield LK API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reports.router, prefix="/reports", tags=["reports"])
app.include_router(areas.router, prefix="/areas", tags=["areas"])
app.include_router(suggest.router, tags=["ai"])


@app.get("/health")
def health():
    return {"status": "ok"}
