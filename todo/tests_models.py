from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_done_defaults_to_False(self):
        item = Item(name="Create a test")
        self.assertEqual(item.name, "Create a test")
        self.assertFalse(item.done)

    def test_can_create_item_with_name_and_status(self):
        item = Item(name="Create a test", done=True)
        self.assertEqual(item.name, "Create a test")
        self.assertTrue(item.done)

    def test_name_is_string(self):
        item = Item(name="Create a test")
        self.assertEqual("Create a test", str(item))