from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI DevOps Incident Analyzer"
    VERSION: str = "1.0.0"
    DEBUG: bool = True


settings = Settings()