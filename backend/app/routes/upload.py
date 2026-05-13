from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
import json
from app.services.schema_guard import detect_schema_drift

from app.services.validator import validate_data
from app.services.cleaner import clean_data

from app.database import SessionLocal
from app.models.upload_model import UploadReport
from app.auth.verify_token import verify_token

from fastapi import Depends

router = APIRouter()


@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    user: str = Depends(verify_token)
):

    # READ CSV
    df = pd.read_csv(file.file)

    # EXPECTED SCHEMA

    expected_schema = {

        "name": "object",

        "email": "object",

        "salary": "int64"
    }

    # ORIGINAL PREVIEW
    original_preview = (
        df.head()
        .fillna("")
        .to_dict(orient="records")
    )

    # VALIDATION
    validation_report = validate_data(df)

    # SCHEMA DRIFT DETECTION

    schema_drift_report = detect_schema_drift(
        df,
        expected_schema
    )

    # CLEANING
    cleaned_df, cleaning_report = clean_data(df)

    # SAVE CLEANED CSV

    cleaned_file_path = (
        f"cleaned_{file.filename}"
    )

    cleaned_df.to_csv(
        cleaned_file_path,
        index=False
    )

    # CLEANED PREVIEW
    cleaned_preview = (
        cleaned_df.head()
        .fillna("")
        .to_dict(orient="records")
    )

    # DATABASE SESSION
    db = SessionLocal()

    # CREATE DATABASE RECORD
    upload_record = UploadReport(
        user_email=user,

        filename=file.filename,

        total_rows=int(len(df)),

        validation_report=json.dumps(
            validation_report
        ),

        cleaning_report=json.dumps(
            cleaning_report
        )
    )

    # SAVE TO DATABASE
    db.add(upload_record)

    db.commit()

    db.close()

    # FINAL RESPONSE
    return {

        "filename": file.filename,

        "columns": list(df.columns),

        "rows": int(len(df)),

        "preview": original_preview,

        "validation_report": validation_report,

        "schema_drift_report": schema_drift_report,

        "cleaning_report": cleaning_report,

        "cleaned_preview": cleaned_preview,

        "download_file": cleaned_file_path,
    }


@router.get("/uploads")
def get_uploads(
    user: str = Depends(verify_token)
):

    db = SessionLocal()

    uploads = db.query(UploadReport).filter(
        UploadReport.user_email == user
    ).all()

    result = []

    for upload in uploads:

        result.append({

            "id": upload.id,

            "filename": upload.filename,

            "total_rows": upload.total_rows,

            "validation_report":
                upload.validation_report,

            "cleaning_report":
                upload.cleaning_report,

            "created_at":
                str(upload.created_at)
        })

    db.close()

    return result

@router.get("/download/{filename}")
def download_file(filename: str):

    file_path = filename

    return FileResponse(

        path=file_path,

        filename=filename,

        media_type='text/csv'
    )

@router.get("/analytics")
def get_analytics(
    user: str = Depends(verify_token)
):

    db = SessionLocal()

    uploads = db.query(UploadReport).filter(
        UploadReport.user_email == user
    ).all()

    total_uploads = len(uploads)

    total_rows = sum(
        upload.total_rows for upload in uploads
    )

    analytics = {
        "total_uploads": total_uploads,
        "total_rows_processed": total_rows
    }

    db.close()

    return analytics

