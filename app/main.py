import uvicorn
from fastapi import FastAPI
from app.api.api_v1.endpoints import posts
from starlette.middleware.cors import CORSMiddleware
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.db.db import db

app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router, prefix=API_PREFIX)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

