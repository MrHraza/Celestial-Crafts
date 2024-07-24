from django.shortcuts import render, redirect
from django.conf import settings
from .forms import OrderForm
from .models import OrderItem, Order
from bag.bag_operations import Bag
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    bag = Bag(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in bag:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            return redirect('order_success')
    else:
        form = OrderForm()

    total_cost = bag.get_total_cost()

    intent = stripe.PaymentIntent.create(
        amount=int(total_cost * 100), 
        currency='gbp',
        automatic_payment_methods={
            'enabled': True,
        },
    )

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'client_secret': intent.client_secret,
        'grand_total': total_cost, 
        'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY
    })

def order_success(request):
    bag = Bag(request)
    bag.clear()
    return render(request, 'checkout/order_success.html')

