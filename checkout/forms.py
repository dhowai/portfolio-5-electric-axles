from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Form for entering order details """
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email',
                'phone_number', 'country', 'postcode',
                'city', 'address', 'apartment_suite_etc',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'postcode': 'Postcode',
            'address': 'Address',
            'apartment_suite_etc': 'Appartment, suite, etc',
            'city': 'City',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
