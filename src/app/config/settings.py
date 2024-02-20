"""
Settings file for project
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__name__).parent
env_path = os.path.join(os.path.dirname(BASE_DIR.absolute()), '.env')
load_dotenv(env_path)


class Settings(BaseSettings):
    """
    Settings class for the project
    """

    DATABASE_URL: str
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'fast-api-currency-converter'

    SECRET_KEY: str
    API_KEY_RATE: str

    # Logging settings
    LOGGING_LEVEL: str = 'INFO'
    LOG_FILE: str = 'app.log'

    model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()
