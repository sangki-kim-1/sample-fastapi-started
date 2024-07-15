import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str = "development"
    app_name: str = "Sample App"
    admin_email: str

    model_config = SettingsConfigDict(env_file=f'{os.getenv("ENVIRONMENT")}.env')