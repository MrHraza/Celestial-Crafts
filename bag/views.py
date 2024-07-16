from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product
from .bag_operations import Bag

def bag_detail(request):
    bag = Bag(request)
    context = {
        'bag': bag,
        'grand_total': bag.get_total_cost(),
    }
    return render(request, 'bag/bag_detail.html', context)

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    bag = Bag(request)
    bag.add(product=product, quantity=quantity)

    messages.success(request, f"{product.name} has been added to your bag.")
    return redirect('product_detail', pk=product_id)

def remove_from_bag(request, product_id):
    """Remove an item from the shopping bag."""
    bag = Bag(request)
    product = get_object_or_404(Product, id=product_id)
    bag.remove(product)
    messages.success(request, f"{product.name} has been removed from your bag.")
    return redirect('bag_detail')