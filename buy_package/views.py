from django.shortcuts import render

# Create your views here.


def buy_package(request):
    '''Return html File'''

    ''' Simple multiply func. that allow user to choose how many months they want to subscribe for! '''
    ''' In order to work our form input we needed to request.POSt.get('input name') '''
    if request.method == 'POST':
        price = 299
        quantity = int(request.POST.get('quantity'))
        total = price * quantity
        return render(request, "buy_package.html", {'total': total, 'price': price, 'quantity': quantity})

    else:
        return render(request, "buy_package.html", {'price': 299, 'total': 299})



