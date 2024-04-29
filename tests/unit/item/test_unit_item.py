import unittest
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from internal.item import service, models
from internal.item.schemas import ItemCreateDto, ItemUpdateDto

TEST_DESCRIPTION = "DESCRIPTION"
TEST_TITLE = "TITLE"
TEST_S3_URL = "http://fdg.com"
TEST_PRICE = 5


class UserTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock = Mock()

    def test_get_item(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = "item"
        item = service.get_item(self.mock, 5)
        assert item == "item"

    def test_get_item__not_found(self):
        self.mock.query.return_value.filter \
            .return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            service.get_item(self.mock, 5)
        assert str(e.value) == "404: Item with id=5 is not found"

    @patch("internal.user.service.get_user")
    def test_get_item_by_user(self, get_user):
        get_user.return_value = "user"
        self.mock.query.return_value.filter\
            .return_value.all.return_value = "item"
        item = service.get_items_by_user(self.mock, 5)
        assert item == "item"

    def test_get_item_by_user__user_not_found(self):
        self.mock.query.return_value.filter\
            .return_value.all.return_value = "item"
        self.mock.query.return_value.filter\
            .return_value.first.return_value = None
        with pytest.raises(HTTPException) as e:
            service.get_items_by_user(self.mock, 5)
        assert str(e.value) == "404: User with id=5 is not found"

    def test_create_item(self):
        self.mock.query.return_value.filter\
            .return_value.all.return_value = "item"
        self.mock.query.return_value.filter\
            .return_value.first.return_value = None
        item_create_dto = ItemCreateDto(
            **{
                "title": TEST_TITLE,
                "description": TEST_DESCRIPTION,
                "s3_url": TEST_S3_URL,
                "price": TEST_PRICE,
                "owner_id": 1
            })

        item = service.create_item(self.mock, item_create_dto)
        assert item.price == TEST_PRICE
        assert item.description == TEST_DESCRIPTION
        assert item.s3_url == TEST_S3_URL
        assert item.title == TEST_TITLE

    def test_delete_item(self):
        result = service.delete_item(self.mock, self.mock)
        assert result is True

    @patch("internal.item.service.get_item")
    def test_update_item(self, get_item):
        get_item.return_value = models.Item(
            title=TEST_TITLE,
            description=TEST_DESCRIPTION,
            s3_url=TEST_S3_URL,
            price=TEST_PRICE,
            owner_id=5,
        )

        item_create_dto = ItemUpdateDto(
            **{
                "id": 1,
                "title": TEST_DESCRIPTION + "a",
                "description": TEST_DESCRIPTION + "a",
                "s3_url": TEST_S3_URL + "a",
                "price": TEST_PRICE + 5,
            })

        item = service.update_item(self.mock, item_create_dto)
        assert item.description == TEST_DESCRIPTION + "a"
        assert item.s3_url == TEST_S3_URL + "a"
        assert item.price == TEST_PRICE + 5
        assert item.owner_id == 5
