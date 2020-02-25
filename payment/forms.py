from django import forms
from .models import Payment


class PackagePaymentForm(forms.Form):

    # THIS IS A LOOP FOR A USER CHOOSE THEIR MONTH AND YEAR EXPIRY DATES
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2030)]

    # THIS IS A STRIPE REQUIREMENT FIELDS(CARD DETAILS) IN ORDER TO COMPLETE A PAYMENT.
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
    # stripe_id = forms.CharField(widget=forms.HiddenInput)


# THIS IS A PAYMENT MODEL CREATED IN THE PAYMENT/MODELS.PY THAT CONTAIS ALL THOSE INFORMATIONS.  
class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'city', 'street_address1', 'street_address2'                      
        )