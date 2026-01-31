# config/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    Application settings, loaded from .env file and environment variables.
    """
    # Telethon API credentials
    TELEGRAM_API_ID: int = 0
    TELEGRAM_API_HASH: str = "your api hash"

    # Gemini API settings
    GEMINI_API_KEY: str = 'your api key'

    # Pydantic settings configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore'  # Ignore extra fields from .env
    )

# Create a single instance of the settings to be used throughout the application
settings = Settings()