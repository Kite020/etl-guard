from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database import Base


class UploadReport(Base):

    __tablename__ = "upload_reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(String)

    total_rows = Column(Integer)

    validation_report = Column(String)

    cleaning_report = Column(String)

    # NEW COLUMN
    # Stores which user uploaded the file
    user_email = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )