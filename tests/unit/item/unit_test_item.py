import unittest
from unittest.mock import Mock

from sqlalchemy.orm import Session

from internal.item import service
from internal.item.models import Item


class ItemServiceTests(unittest.TestCase):
    def setUp(self):
        self.db_session_mock = Mock(spec=Session)

    # not working
    def test_get_item_existing_item(self):
        # Mock the database session and item
        item_mock = Mock()
        self.db_session_mock.query().filter().first().return_value = create_item()

        item = service.get_item(self.db_session_mock, 1)

        self.assertEqual(item.id, item_mock.id)


def create_item():
    item = Item()
    item.id = 1
    item.owner_id = 1
    item.title = "title"
    item.price = 150
    item.description = "description"
    item.s3_url = "http://"
    return item

if __name__ == '__main__':
    unittest.main()
