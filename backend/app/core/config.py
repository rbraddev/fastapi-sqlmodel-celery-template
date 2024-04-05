import os
import pathlib
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "development")
    DATABASE_URL: str = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict = {}
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379/0")
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")


class DevelopmentSettings(Settings):
    pass


class ProductionSettings(Settings):
    pass


class TestingSettings(Settings):
    DATABASE_URL: str = "sqlite:///./test.db"
    DATABASE_CONNECT_DICT: dict = {"check_same_thread": False}


@lru_cache()
def get_settings() -> Settings:
    config_cls_dict = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
        "testing": TestingSettings
    }

    config_name = os.environ.get("ENVIRONMENT", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()