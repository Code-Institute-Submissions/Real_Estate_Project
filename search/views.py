from django.shortcuts import render
from listing.models import Listing


# Create your views here.


def buy_search(request):
    listing = Listing.objects.filter(buy=True)
    return render(request, "buy.html", {"listing": listing})


def rent_search(request):
    listing = Listing.objects.filter(rent=True)
    return render(request, "rent.html", {"listing": listing})


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
