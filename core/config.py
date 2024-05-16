import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import models as models
from typing import List

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'FASTAPI')
    # SECRET_KEY = os.getenv('SECRET_KEY', '')
    API_PREFIX: str  = ''
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    DATABASE_URL: str = os.getenv('DATABASE_URL', '')
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    SECURITY_ALGORITHM: str = 'HS256'
    LOGGING_CONFIG_FILE: str = os.path.join(BASE_DIR, 'log_conf.yaml')


settings = Settings()


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(
        database=client.get_default_database(), document_models=models.__all__
    )

