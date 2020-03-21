from django.test import TestCase
from .models import Listing

# Create your tests here.


class ListingTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_listing(self):
        list = Listing(True)
        self.assertTrue(list, True)


