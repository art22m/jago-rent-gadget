import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker

from bin.main import create_app
from internal.data.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()



@pytest.fixture
def app():
    app = create_app()
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_db] = override_get_db
    return app

@pytest.fixture
def client(app):
    return TestClient(app)
