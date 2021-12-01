from django.forms import ModelForm
from .models import *

class order_form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class customer_form(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
