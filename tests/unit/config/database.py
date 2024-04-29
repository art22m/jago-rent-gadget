from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from internal.data.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


def init_db():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
