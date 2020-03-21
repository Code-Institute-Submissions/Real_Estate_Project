from django.test import TestCase
from .models import Signup


class TestModelSignup(TestCase):
    '''
    def setUp(self):
        self.signup = Signup.object.create(
            name='Signup 1',
            price=1000

        )
    '''
    def test_model_signup(self):
        signup = Signup(name='Test')
        self.assertEqual(signup.name, 'Test')
        