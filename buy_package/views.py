from django.shortcuts import render, redirect, reverse

# Create your views here.


def buy_package(request):
    return render(request, 'buy_package.html')


def add_to_buy_package(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('buy_package'))


def adjust_buy_package(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('buy_package'))




















''' 
def buy_package(request):
   
    if request.method == 'POST':
        price = 299
        quantity = int(request.POST.get('quantity'))
        total = price * quantity
        return render(request, "buy_package.html", {'total': total, 'price': price, 'quantity': quantity})

    else:
        return render(request, "buy_package.html", {'price': 299, 'total': 299})

'''


