"""
Settings file for project
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__name__).parent
env_path = os.path.join(os.path.dirname(BASE_DIR.absolute()), ".env")
load_dotenv(env_path)


class Settings(BaseSettings, frozen=True):
    """
    Settings class for the project
    """

    model_config = SettingsConfigDict(env_file=".env")
    # model_config = SettingsConfigDict(env_file=env_path)

    DEBUG: bool = False

    PROJECT_NAME: str = "fast-api-currency-exchanger"
    API_V1_STR: str = "/api/v1"

    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/currency_converter"
    )

    SECRET_KEY: str
    API_KEY_RATE: str

    HOST: str = "0.0.0.0"
    PORT: int = 8001

    # Logging settings
    LOGGING_LEVEL: str = "INFO"
    LOG_FILE: str = "app.log"

    SYS_CURRENCY: str = "USD"


settings = Settings()
