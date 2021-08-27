from pydantic import BaseSettings, Field

_DB_RX = r"^(sqlite)://.+$"


class Settings(BaseSettings):
    DATABASE_URL: str = Field("sqlite:///./sqlite.db?check_same_thread=true", regex=_DB_RX)

    class Config:
        env_file = ".env"


settings = Settings()
