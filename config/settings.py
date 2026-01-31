# config/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings, loaded from .env file and environment variables.
    """
    # Telethon API credentials
    TELEGRAM_API_ID: int
    TELEGRAM_API_HASH: str

    # Google ADK (Dialogflow) settings
    GOOGLE_PROJECT_ID: str
    GOOGLE_APPLICATION_CREDENTIALS_PATH: str

    # Pydantic settings configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore'  # Ignore extra fields from .env
    )

# Create a single instance of the settings to be used throughout the application
settings = Settings()