from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('default_full_name','default_phone_number', 'default_country', 'default_postcode',
                  'default_town_or_city', 'default_street_address1', 'default_street_address2', 'default_county')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['default_full_name'].widget.attrs['placeholder'] = ''
        self.fields['default_phone_number'].widget.attrs['placeholder'] = ''
        self.fields['default_country'].widget.attrs['placeholder'] = ''
        self.fields['default_postcode'].widget.attrs['placeholder'] = ''
        self.fields['default_town_or_city'].widget.attrs['placeholder'] = ''
        self.fields['default_street_address1'].widget.attrs['placeholder'] = ''
        self.fields['default_street_address2'].widget.attrs['placeholder'] = ''
        self.fields['default_county'].widget.attrs['placeholder'] = ''
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
