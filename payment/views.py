from django.shortcuts import render, reverse, redirect
from django.conf import settings
import stripe
from .forms import PaymentForm, PackagePaymentForm
from django.utils import timezone
from buy_package.views import buy_package
from django.contrib import messages


# OUR VIEW REQUIRES A STRIPE API KEY TO WORK / we nedd to import settings and stripe.
stripe.api_key = settings.STRIPE_SECRET_KEY


def payout(request):
    # payment_form and  package_payment_form will contain our form made in forms.py 
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        package_payment_form = PackagePaymentForm(request.POST)

        ''' payment_form and package_payment_form is valid. that is that they've been filled out correctly,
        then the payment form will be saved as payment.
        And the payment date will be timezone.now, so it will take the time that the button was hit.
        So then we can save that payment''' 
        
        if payment_form.is_valid() and package_payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.date = timezone.now()
            payment.save()
        
            # buy_package = request.session.get('buy_package', {})
            total = buy_package.total
            total.save()
            
            # try except will create a customer charge. So that's using Stripe's in-built API.
            try:
                customer = stripe.Charge.create(
                    # amount will always need to be multipy * 100 in stripe because uses penny(cents).
                    amount=int(total * 100),
                    currency="GBP",
                    # the description allow us to see who pay us in stripe dashboard.
                    description=request.full_name,
                    # the stripe id also show us the id hidden in the forms.py/payment.
                    card=package_payment_form.cleaned_data['stripe_id']
                )
            # the stripe itself will do all the payment prossess check and security, but it's needed to send a user a message
            # if anything goes wrong, as declined payment also if payment is accept or any other issue.
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "Thank you, You have purchased our Package!")
                return redirect(reverse('create_user'))

            else:
                messages.error(request, "Unable to take payment")

        else:
            print(package_payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")

    # im just returning a blank form.
    else:
        package_payment_form = PackagePaymentForm()
        payment_form = PaymentForm()
    
    return render(request, "payment.html", {"payment_form": payment_form, 
                                            "package_payment_form": package_payment_form, 
                                            "publishable": settings.STRIPE_PUBLISHABLE_KEY})
