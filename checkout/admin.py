from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price')  
    extra = 0  
    readonly_fields = ('product', 'quantity', 'price')  

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    fields = ('full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city',
              'street_address1', 'street_address2', 'county')
    list_display = ('full_name', 'email', 'phone_number')

admin.site.register(Order, OrderAdmin)
