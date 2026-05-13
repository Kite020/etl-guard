from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.upload_model import UploadReport
from app.database import Base
from app.models.user_model import User
from app.routes.auth import router as auth_router

from app.routes.upload import router as upload_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "ETL Guard Backend Running"}