from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_detail, name='bag_detail'),
    path('add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<int:product_id>/', views.remove_from_bag, name='remove_from_bag'),
]
