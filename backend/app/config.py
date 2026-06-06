from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI DevOps Incident Analyzer"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password29"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "ai_incident_db"

settings = Settings()