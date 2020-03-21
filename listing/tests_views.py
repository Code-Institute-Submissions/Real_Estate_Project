from django.test import TestCase, Client
# from django.shortcuts import get_object_or_404
from .models import Listing
from django.urls import reverse


class TestViewsFunc(TestCase):

    def test_add_property(self):
        client = Client()
        response = client.get(reverse('add_property'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "addproperty.html")
    
    def test_edit_property(self):
        list = Listing(title="Create a Test")
        list.save()
        page = self.client.get("/edit/{0}".format(list.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "editdetails.html")

    def test_delete(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)


'''
    def test_property_detail(self):
        page = get_object_or_404(Listing, pk=id)
        self.assertEqual(page.done, True)
'''
    
        
