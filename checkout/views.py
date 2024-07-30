from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from .forms import OrderForm
from .models import Order, OrderItem
from bag.bag_operations import Bag
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    bag = Bag(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            order = form.save(commit=False)
            order.date = timezone.now() 
            order.save() 
            print(f"Order created: {date}")
            
            for item in bag:
                try:
                    product = item['product']
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=item['quantity'],
                        price=item['price'],
                    )
                    order_item.save()
                    print(f"Order item created: {order_item}")
                except Product.DoesNotExist:
                    print(f"Product with id {item['product'].id} does not exist")
                    continue

            bag.clear() 
            print("Bag cleared")
            return redirect('order_success')

        else:
            print("Form is invalid")
            print(form.errors)
    else:
        print("GET request received")
        form = OrderForm()

    total_cost = bag.get_total_cost()

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'stripe_publishable_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': stripe.PaymentIntent.create(
            amount=int(total_cost * 100),
            currency=settings.STRIPE_CURRENCY,
            automatic_payment_methods={'enabled': True},
        ).client_secret
    })

def order_success(request):
    return render(request, 'checkout/order_success.html')
