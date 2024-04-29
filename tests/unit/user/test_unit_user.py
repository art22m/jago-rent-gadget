import unittest
from unittest.mock import Mock
from fastapi import HTTPException

import pytest
from requests import HTTPError

from internal.user import service
from internal.user.schemas import UserCreateDto

TEST_EMAIL = "test@gmail.com"
TEST_PASSWORD = "123"  # nosec
TEST_NAME = "Igor"
TEST_SESSION = "123"


class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()

    def test_create_user(self):
        self.mock.create_user_with_email_and_password.return_value = {
            "sessionId": TEST_SESSION
        }
        user = UserCreateDto(
            **{
                "email": TEST_EMAIL,
                "password": TEST_PASSWORD,
                "name": TEST_NAME,
            }
        )
        user = service.create_user(self.mock, self.mock, user)
        assert user["sessionId"] == TEST_SESSION
        assert user["name"] == TEST_NAME

    def test_create_user__firebase_http_error(self):
        self.mock. \
            create_user_with_email_and_password. \
            side_effect = HTTPError({"error1": "error"}, '{"error": {"code": "404", "message": "Not found"}}')
        with pytest.raises(HTTPException) as e:
            service.create_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "404: Not found"

    def test_create_user__unexpected_error(self):
        self.mock. \
            create_user_with_email_and_password. \
            side_effect = Exception()
        with pytest.raises(HTTPException) as e:
            service.create_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "500: An internal server error occurred. Try again later. "

    def test_get_user(self):
        self.mock.query.return_value.filter.return_value.first.return_value = "user"
        user = service.get_user(self.mock, 5)
        assert user == "user"

    def test_get_user__not_found(self):
        self.mock.query.return_value.filter.return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            user = service.get_user(self.mock, 5)
        assert str(e.value) == "404: User with id=5 is not found"

    def test_get_user_by_email(self):
        self.mock.query.return_value.filter.return_value.first.return_value = "user"
        user = service.get_user_by_email(self.mock, "email")
        assert user == "user"

    def test_get_user_by_email__not_found(self):
        self.mock.query.return_value.filter.return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            user = service.get_user_by_email(self.mock, "email")
        assert str(e.value) == "404: User with email=email is not found"
