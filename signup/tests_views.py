from django.test import TestCase, Client
from .models import Signup
from django.urls import reverse
# Create your tests here.


class TestViewSignup(TestCase):

    def test_signup(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")

        
         
        
        