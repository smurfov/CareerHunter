from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "React FastAPI Backend"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"

    # Добавляем настройки сервера
    HOST: str = "localhost"
    PORT: int = 8000
    RELOAD: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
