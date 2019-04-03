from django.test import TestCase
from .forms import ItemForm

# ToDo Item Form tests

class TestForms(TestCase):

    def test_CanCreateAnItemWithJustAName(self):
        form = ItemForm({"name": "Create Tests"})
        self.assertTrue(form.is_valid())

    def test_CorrectMessageForMissingName(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])