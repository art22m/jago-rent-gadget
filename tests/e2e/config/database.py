import os

from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from internal.data.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.abspath(os.getcwd()) + "/tests/e2e/config/test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
