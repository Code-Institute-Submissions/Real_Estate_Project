from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Listing
from .forms import ListingAddForm
from django.contrib import messages
from django.conf import settings


def add_property(request):   
    if request.method == 'POST':
        form = ListingAddForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
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


def property_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.save()

    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'listing': listing
    }
    return render(request, "propertydetail.html", context)


def edit_property(request, pk):
    listing = Listing.objects.get(pk=pk)
    if request.method == "POST":
        form = ListingAddForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect('property_detail', listing.pk)
    else:
        form = ListingAddForm(instance=listing)
    return render(request, 'editdetails.html', {'form': form})
    # redirected to add property just added a new property


def delete(request, pk):
    listing = Listing.objects.get(pk=pk)
    listing.delete()
    return redirect(reverse('view_property'), {'listing': listing})








