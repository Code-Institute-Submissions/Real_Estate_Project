from django.shortcuts import render
from .models import Signup

# Create your views here.


def signup(request):
    '''Return html File'''
    signup = Signup.objects.all()
    return render(request, "signup.html", {'signup': signup})