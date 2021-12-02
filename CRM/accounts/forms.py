from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class order_form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class customer_form(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
