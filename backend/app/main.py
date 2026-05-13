from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ETL Guard Backend Running"}