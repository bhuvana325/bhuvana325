from django.test import TestCase
from .models import products


# Create your tests here.
class Basictests(TestCase):
    def setup(self):
        products.objects.create(name='Samsung',
                                description='Good',
                                costperitem=30000,
                                stockquantity=20,
                                volume=600000)

    def test_get_method(self):
        url = "http://127.0.0.1:8000/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = products.objects.filter(name='Samsung')
        self.assertEqual(qs.count(), 0)
