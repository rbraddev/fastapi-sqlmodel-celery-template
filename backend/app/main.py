from fastapi import FastAPI

from app.api import api_router
from app.core.celery import create_celery
import app.tasks

app = FastAPI()
app.include_router(api_router)
celery = create_celery()