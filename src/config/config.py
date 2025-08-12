from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """
    # Define your configuration variables here
    app_name: str = "McAstr PA Service"
    version: str = "1.0.0"
    debug: bool = True

    class Config:
        env_file = ".env"  # Load environment variables from .env file
        env_file_encoding = "utf-8"

settings = Settings()