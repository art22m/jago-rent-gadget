import random
import string

import pytest
from fastapi.testclient import TestClient

from bin.main import create_app
from internal.data.auth import pb_auth
from internal.data.database import get_db
from tests.e2e.config.auth import override_pb_auth
from tests.e2e.config.database import override_get_db


@pytest.fixture
def app():
    app = create_app()
    # Подменяем продовую базу на тестовую и мокируем ответ firebase
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[pb_auth] = override_pb_auth
    return app


@pytest.fixture
def client(app):
    return TestClient(app)


def generate_random_email():
    domain = "google.com"  # Replace with your desired domain name
    username_length = random.randint(
        5, 10
    )  # Random username length between 5 and 10
    username = "".join(
        random.choices(string.ascii_lowercase, k=username_length)
    )
    email = f"{username}@{domain}"
    return email
