# from celery import Celery
from celery import current_app
from celery.local import Proxy
from app.core.config import settings


def create_celery() -> Proxy:
    celery_app = current_app
    celery_app.config_from_object(settings, namespace="CELERY")
    return celery_app