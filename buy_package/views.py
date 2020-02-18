from django.shortcuts import render

# Create your views here.


def buy_package(request):
    '''Return html File'''
    return render(request, "buy_package.html")