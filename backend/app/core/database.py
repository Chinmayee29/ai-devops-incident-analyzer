from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

from app.models.base import Base
from app.models.incident import Incident

Base.metadata.create_all(bind=engine)