from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.request_log import RequestLogCreate, RequestLogOut
from app.services import request_log as log_service

router = APIRouter(prefix="/logs", tags=["logs v1"])


@router.post("", response_model=RequestLogOut, status_code=201)
def create_log(data: RequestLogCreate, db: Session = Depends(get_db)):
    return log_service.create_log(db, data)


@router.get("", response_model=list[RequestLogOut])
def list_logs(db: Session = Depends(get_db)):
    return log_service.list_logs(db)