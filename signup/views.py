from django.shortcuts import render
from .models import Signup

# Create your views here.


def signup(request):
    '''Return html File'''
    price = int(299)
    return render(request, "signup.html", {"price": price})