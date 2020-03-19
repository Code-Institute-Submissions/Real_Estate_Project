from django.shortcuts import render
from listing.models import Listing
from django.core.paginator import Paginator

# Create your views here.


def buy_search(request):
    
    listing = Listing.objects.filter(buy=True)
    paginator = Paginator(listing, 6)
    page = request.GET.get('page', 1) 
    listing = paginator.page(page)
    return render(request, "buy.html", {"listing": listing})
    
    
def rent_search(request):
    listing = Listing.objects.filter(rent=True)
    
    paginator = Paginator(listing, 6)
    page = request.GET.get('page', 1) 
    listing = paginator.page(page)
    return render(request, "rent.html", {"listing": listing})


def search_all(request):
      
    listing = Listing.objects.all()
    
    # im getting the request from user
    bedroom_query = None if request.GET.get('bed') == 'Bedrooms' else request.GET.get('bed')
    city_query = None if request.GET.get('city') == 'City' else request.GET.get('city')
    min_price_query = None if request.GET.get('min_price') == 'Min Price' else request.GET.get('min_price')
    max_price_query = None if request.GET.get('max_price') == 'Max Price' else request.GET.get('max_price')
    buy_rent_query = None if request.GET.get('buy_rent') == 'Buy or Rent' else request.GET.get('buy_rent')
     
    # filtering the result as they want to find the specific product
    if bedroom_query:
        listing = listing.filter(bedrooms=bedroom_query)
   
    if city_query:
        listing = listing.filter(city=city_query)
    
    if min_price_query:
        listing = listing.filter(price__gte=min_price_query)
 
    if max_price_query:
        listing = listing.filter(price__lte=max_price_query)

    if buy_rent_query:
        if buy_rent_query == 'buy':
            listing = listing.filter(buy=True)
        if buy_rent_query == 'rent':
            listing = listing.filter(rent=True)
    
    paginator = Paginator(listing, 6)
    page = request.GET.get('page', 1) 
    listing = paginator.page(page)
        
    return render(request, "search.html", {"listing": listing})
