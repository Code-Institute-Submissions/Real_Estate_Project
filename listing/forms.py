from django import forms
from .models import Listing


class ListingAddForm(forms.ModelForm):
    class Meta:
        model = Listing

        fields = ['title', 'buy', 'rent', 'price', 'address', 'city', 'postcode', 'rooms',
                  'bedrooms', 'bathrooms', 'sqft', 'garage', 'garden', 'photos',
                  'description', 'published_date', 'user']

''' 
THE FIELDS ARE THOSE CREATED ON MODELS.PY FILE
the fields that we're going to have on our form are user editable fields
'''
