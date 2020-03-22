from django import forms
from .models import Listing


class ListingAddForm(forms.ModelForm):
    class Meta:
        model = Listing

        fields = ['title', 'sale', 'rent', 'price', 'address', 'city', 'postcode', 'rooms',
                  'bedrooms', 'bathrooms', 'sqft', 'garage', 'garden', 'photos', 'photo1', 'photo2',
                  'description', 'published_date', 'user']



