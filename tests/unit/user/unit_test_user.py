import unittest
from unittest.mock import Mock

import requests

from internal.user import service
from internal.user.schemas import UserCreateDto

TEST_EMAIL = "test@gmail.com"
TEST_PASSWORD = "123"
TEST_NAME = "Igor"


class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()

    def test_create_user(self):
        self.mock.create_user_with_email_and_password.return_value = "success"
        user = UserCreateDto(**{
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD,
            "name": TEST_NAME
        })
        user = service.create_user(self.mock, self.mock, user)
        assert user.email == TEST_EMAIL
        assert user.name == TEST_NAME

    def test_create_user__firebase_error(self):
        self.mock.create_user_with_email_and_password.return_value.side_effect = requests.exceptions.HTTPError(
            500, "meow")
