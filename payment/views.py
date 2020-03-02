from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
import stripe
from .forms import PaymentForm, PackagePaymentForm
from django.utils import timezone
from django.contrib import messages
from signup.models import Signup
from .models import OrderLineItem

# from django.utils.crypto import get_random_string


stripe.api_key = settings.STRIPE_SECRET


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
                
            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                signup = get_object_or_404(Signup, pk=id)
                total += quantity * signup.price
                order_line_item = OrderLineItem(
                    payment=payment,
                    signup=signup,
                    quantity=quantity
                )
                order_line_item.save()
                               
            # try except will create a customer charge. So that's using Stripe's in-built API.
            try:
                customer = stripe.Charge.create(
                    # amount will always need to be multipy * 100 in stripe because uses penny(cents).
                    amount=int(total * 100),
                    currency="gbp",
                    source="tok_mastercard",
                    
                    # description=Payment.full_name                
                    # the stripe id also show us the id hidden in the forms.py/payment.
                    # card=payment_form.cleaned_data['stripe_id']
                    # payment_form from JS.
                )
            # the stripe itself will do all the payment prossess check and security, but it's needed to send a user a message
            # if anything goes wrong, as declined payment also if payment is accept or any other issue.
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            # the original idea for this part is (if customer.paid:):
            # 1 - generate a code display to user to the user can match in the register page. 
            # /or/
            # 2 - request a user email address and send a email with the register link (sha and salted in the dns)
            # also need some code to be uesed once to prevent anyone to get the link and add to the website.

            if customer.paid:
                messages.error(request, "Thank you, You have purchased our Package!")
                request.session['cart'] = {}
                return redirect(reverse('registration'))

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
                                            "publishable": settings.STRIPE_PUBLISHABLE
                                            })
