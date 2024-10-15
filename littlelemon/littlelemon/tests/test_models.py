from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_menu_item(self):
        item = Menu.objects.create(title="Ice Cream", price=3, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 3")