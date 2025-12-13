from pydantic_settings import BaseSettings
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = True

settings = Settings()