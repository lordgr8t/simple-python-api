from sqlalchemy.orm import Session

from app.models.request_log import RequestLog
from app.schemas.request_log import RequestLogCreate


def create_log(db: Session, data: RequestLogCreate) -> RequestLog:
    log = RequestLog(
        ip=data.ip,
        endpoint=data.endpoint,
        method=data.method,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def list_logs(db: Session) -> list[RequestLog]:
    return db.query(RequestLog).order_by(RequestLog.created_at.desc()).all()