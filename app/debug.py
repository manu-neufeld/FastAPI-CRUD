import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.api_v1.api import api_router
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "debug.env"), override=True)

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)