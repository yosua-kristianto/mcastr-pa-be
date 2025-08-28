from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Configuration settings for the application.
    """
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str

    secret: str

    # Define your configuration variables here
    app_name: str = "McAstr PA Service"
    version: str = "1.0.0"
    app_debug: bool
    app_env: str
    

    class Config:
        env_file = ".env"  # Load environment variables from .env file
        env_file_encoding = "utf-8"

settings = Settings()