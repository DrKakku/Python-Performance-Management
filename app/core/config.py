from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI Application"
    API_V1_STR: str = "/api/v1"

settings = Settings()