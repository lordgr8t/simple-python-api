from fastapi import FastAPI

from app.database import Base, engine
from app.api.v1.router import router as v1_router

from app.models import request_log  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Simple API",
    version="1.0.0",
)

app.include_router(v1_router)


@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs", "version": "v1"}