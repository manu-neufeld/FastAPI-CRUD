from fastapi import APIRouter

from app.api.api_v1.endpoints import posts, ping

api_router = APIRouter()
api_router.include_router(posts.router, tags=["post"])
api_router.include_router(ping.router, tags=["ping"])