from fastapi import APIRouter

from app.api.v1.request_logs import router as logs_router

router = APIRouter(prefix="/api/v1")

router.include_router(logs_router)