import unittest
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from internal.item import service


class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()

    def test_get_item(self):
        self.mock.query.return_value.filter.return_value.first.return_value = "item"
        item = service.get_item(self.mock, 5)
        assert item == "item"

    def test_get_item__not_found(self):
        self.mock.query.return_value.filter.return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            service.get_item(self.mock, 5)
        assert str(e.value) == "404: Item with id=5 is not found"

    @patch("internal.user.service.get_user")
    def test_get_item_by_user(self, get_user):
        get_user.return_value = "user"
        self.mock.query.return_value.filter.return_value.all.return_value = "item"
        item = service.get_items_by_user(self.mock, 5)
        assert item == "item"

    @patch("internal.user.service.get_user")
    def test_get_item_by_user__user_not_found(self, get_user):
        get_user.side_effect = HTTPException(
            status_code=404, detail=f"User with id=5 is not found"
        )
        self.mock.query.return_value.filter.return_value.all.return_value = "item"
        with pytest.raises(HTTPException) as e:
            service.get_items_by_user(self.mock, 5)
        assert str(e.value) == "404: User with id=5 is not found"

