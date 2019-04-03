from django.test import TestCase
from .models import Item

# ToDo Views testing

class TestViews(TestCase):

    def test_GetHomePage(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
    

    def test_GetAddItemPage(self):
        page = self.client.get("/add-item")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item-form.html")

    def test_GetEditItemPage(self):
        item = Item(name="Create a Test")
        item.save()

        page = self.client.get("/edit-item/{}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item-form.html")
    
    def test_GetEditItemPageForNonExistantItem(self):
        page = self.client.get("/edit-item/1")
        self.assertEqual(page.status_code, 404)