from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2', 'county'
        )

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'required': 'required'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'required': 'required'}),
            'country': forms.TextInput(attrs={'class': 'form-control',
                                              'required': 'required'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control',
                                               'required': 'required'}),
            'town_or_city': forms.TextInput(attrs={'class': 'form-control',
                                                   'required': 'required'}),
            'street_address1': forms.TextInput(attrs={'class': 'form-control',
                                                      'required': 'required'}),
            'street_address2':
                forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control'}),
        }
