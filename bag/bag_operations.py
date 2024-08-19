from decimal import Decimal
from products.models import Product


class Bag:
    def __init__(self, request):
        self.session = request.session
        bag = self.session.get('bag')
        if not bag:
            bag = self.session['bag'] = {}
        self.bag = bag

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.bag:
            self.bag[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        self.bag[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def get_total_cost(self):
        total = Decimal('0.00')
        for item in self.bag.values():
            total += Decimal(item['price']) * item['quantity']
        return total

    def __iter__(self):
        product_ids = self.bag.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.bag[str(product.id)]['product'] = product

        for item in self.bag.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def remove(self, product):
        if str(product.id) in self.bag:
            del self.bag[str(product.id)]
            self.save()

    def clear(self):
        del self.session['bag']
        self.save()