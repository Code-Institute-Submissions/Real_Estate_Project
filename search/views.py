from django.shortcuts import render
from listing.models import Listing
from django.contrib.auth.models import User
from django.db.models import Q
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


def search_all(request):
      
    listing = Listing.objects.all()
    query = None if request.GET.get('bed') == 'Bedrooms' else request.GET.get('bed')
    query1 = None if request.GET.get('city') == 'City' else request.GET.get('city')
    query2 = None if request.GET.get('price') == 'Price' else request.GET.get('price')
      
    if query:
        listing = listing.filter(bedrooms=query)
    if query1:
        listing = listing.filter(city=query1)
    if query2:
        listing = listing.filter(price__lte=query2)
        
    return render(request, "search.html", {"listing": listing})


'''
     Q(address__contains=query) |
            Q(city__contains=query) |
            Q(postcode__contains=query) |
            Q(bathrooms__contains=query) |
            Q(bedrooms__contains=query) |
            Q(rooms__contains=query) |
            Q(price__contains=query) |
            Q(garage__contains=query) |
            Q(garden__contains=query) |
            Q(sqft__contains=query) |
            Q(title__contains=query) |
            Q(buy__contains=query) |
            Q(rent__contains=query)
'''