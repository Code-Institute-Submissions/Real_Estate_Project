from django.shortcuts import get_object_or_404
from signup.models import Signup


def buy_package_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    signup_count = 0
    
    for id, quantity in cart.items():
        signup = get_object_or_404(Signup, pk=id)
        total += quantity * signup.price
        signup_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'signup': signup})
    
    return {'cart_items': cart_items, 'total': total, 'signup_count': signup_count}