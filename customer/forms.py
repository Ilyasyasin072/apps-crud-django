from django import forms
from .models import Customers


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name_customers', 'address_customers', 'phone']
        labels = {
            'name_customers': 'Fullname Customers',
            'address_customers': 'Address Customer'
        }
