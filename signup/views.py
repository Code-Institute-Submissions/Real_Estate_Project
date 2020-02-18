from django.shortcuts import render

# Create your views here.


def signup(request):
    '''Return html File'''
    return render(request, "signup.html")