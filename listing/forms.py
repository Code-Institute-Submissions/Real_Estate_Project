from django import forms
from .models import Listing


class ListingAddForm(forms.ModelForm):
    class Meta:
        model = Listing

        fields = ['title', 'buy', 'rent', 'price', 'address', 'city', 'postcode', 'rooms',
                  'bedrooms', 'bathrooms', 'sqft', 'garage', 'garden', 'photos',
                  'description', 'published_date', 'user']


class ContactFrom(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    email = forms.EmailField(label='email', max_length=50)
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', widget=forms.Textarea)



