from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
]
