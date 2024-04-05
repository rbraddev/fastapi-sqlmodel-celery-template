from fastapi import APIRouter

from app.api.routes import health, users, tasks


api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(tasks.router, tags=["tasks"])