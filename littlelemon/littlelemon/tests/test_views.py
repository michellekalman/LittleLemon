from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Tiramisu", price=4.5, inventory=24)
        self.item2 = Menu.objects.create(title="Greek Salad", price=8, inventory=50)
    def test_getall(self):
        self.assertEqual(str(self.item1), "Tiramisu : 4.5")
        self.assertEqual(str(self.item2), "Greek Salad : 8")