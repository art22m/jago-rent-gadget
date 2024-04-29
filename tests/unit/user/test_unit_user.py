import unittest
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException
from requests import HTTPError

from internal.user import models, service
from internal.user.schemas import UserCreateDto, UserUpdateDto

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
            side_effect = HTTPError(
                {"error1": "error"},
                '{"error": {"code": "404", "message": "Not found"}}'
            )
        with pytest.raises(HTTPException) as e:
            service.create_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "404: Not found"

    def test_create_user__unexpected_error(self):
        self.mock. \
            create_user_with_email_and_password. \
            side_effect = Exception()
        with pytest.raises(HTTPException) as e:
            service.create_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "500: An internal server error" \
                               " occurred. Try again later. "

    @patch("internal.user.service.get_user")
    def test_update_user(self, get_user_method):
        get_user_method.return_value = models.User(
            name=TEST_NAME,
            email=TEST_EMAIL
        )
        user = UserUpdateDto(
            **{
                "id": 1,
                "email": TEST_EMAIL + "a",
                "name": TEST_NAME + "b",
            }
        )
        user = service.update_user(self.mock, user)
        assert user.email == TEST_EMAIL + "a"
        assert user.name == TEST_NAME + "b"

    @patch("internal.user.service.get_user")
    def test_update_user__not_found(self, get_user):
        get_user.return_value = None
        user = UserUpdateDto(
            **{
                "id": 1,
                "email": TEST_EMAIL + "a",
                "name": TEST_NAME + "b",
            }
        )
        with pytest.raises(HTTPException) as e:
            service.update_user(self.mock, user)
        assert str(e.value) == "404: User with " \
                               "id=1 is not found"

    def test_get_user(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = "user"
        user = service.get_user(self.mock, 5)
        assert user == "user"

    def test_get_user__not_found(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            service.get_user(self.mock, 5)
        assert str(e.value) == "404: User with id=5 is not found"

    def test_get_user_by_email(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = "user"
        user = service.get_user_by_email(self.mock, "email")
        assert user == "user"

    def test_get_user_by_email__not_found(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            service.get_user_by_email(self.mock, "email")
        assert str(e.value) == "404: User with email=email is not found"

    def test_signin_user__http_error(self):
        self.mock. \
            sign_in_with_email_and_password. \
            side_effect = HTTPError(
                {"error1": "error"},
                '{"error": {"code": "404", "message": "Not found"}}'
            )
        with pytest.raises(HTTPException) as e:
            service.signin_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "404: Not found"

    def test_signin_user__unexpected_error(self):
        self.mock. \
            sign_in_with_email_and_password. \
            side_effect = Exception
        with pytest.raises(HTTPException) as e:
            service.signin_user(self.mock, self.mock, self.mock)
        assert str(e.value) == "500: An internal server" \
                               " error occurred. Try again later. "

    @patch("internal.user.service.get_user_by_email")
    def test_signin_user(self, get_user_by_email):
        get_user_by_email.return_value = models.User(
            name=TEST_NAME,
            email=TEST_EMAIL
        )
        self.mock.sign_in_with_email_and_password.return_value = {
            "sessionId": TEST_SESSION,
            "email": TEST_EMAIL
        }
        user = service.signin_user(self.mock, self.mock, self.mock)
        assert user["sessionId"] == TEST_SESSION
        assert user["name"] == TEST_NAME
