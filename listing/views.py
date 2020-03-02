from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listing
from .forms import ListingAddForm

from django.contrib import messages
# from django.contrib.auth.models import User


def add_property(request):
    
    if request.method == 'POST':
        form = ListingAddForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            #   user = form.cleaned_data['user']
            messages.success(request, 'Property Saved!')
            form = ListingAddForm()
            
        else:
            messages.error(request, 'Property not saved!')
    
    else:
        form = ListingAddForm()
    context = {
        'form': form
    }

    return render(request, 'addproperty.html', context)


def view_property(request):
    
    user = request.user
    listing = Listing.objects.filter(user=request.user).order_by('-published_date')
    template = 'viewlisting.html'
    return render(request, template, {'listing': listing, 'user': user})