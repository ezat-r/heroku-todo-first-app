from django.test import TestCase
from .models import Item

# ToDo Models testing

class TestModels(TestCase):

    def test_StatusDefaultsToFalse(self):
        # create a dummy item
        item = Item(name="Create a Test")
        item.save()

        self.assertEqual(item.name, "Create a Test")
        self.assertFalse(item.done)
    

    def test_CanCreateAnItemWithNameAndStatus(self):
        # create a dummy item
        item = Item(name="Create a Test", done=True)
        item.save()

        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)