from fastapi import FastAPI
import databases
import sqlalchemy


''' FastAPI CONFIGURATION '''
app = FastAPI(title="FastAPI CRUD Example", docs_url="/docs", redoc_url="/redocs")


''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://postgres:docker@localhost:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)


''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
