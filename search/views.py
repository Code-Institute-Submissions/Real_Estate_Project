from django.shortcuts import render
from listing.models import Listing
from django.contrib.auth.models import User
# Create your views here.


def buy_search(request):
    listing = Listing.objects.filter(buy=True)
    return render(request, "buy.html", {"listing": listing})


def rent_search(request):
    listing = Listing.objects.filter(rent=True)
    return render(request, "rent.html", {"listing": listing})


def agency_search(request):
    user = User.objects.all()
    return render(request, "agents.html", {"user": user})