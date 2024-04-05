from fastapi import APIRouter

from app.api.dependancies import SettingsDep

router = APIRouter()

@router.get("/ping")
async def pong(settings: SettingsDep):
    return {
        "ping": "pong!",
        "environment": settings.ENVIRONMENT
    }