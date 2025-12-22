import os
from pydantic_settings import BaseSettings
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


class AuthSettings(BaseSettings):
    ALGORITHM: str = "HS256"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = False

    AuthSettings()


settings = Settings()
auth_settings = AuthSettings()
