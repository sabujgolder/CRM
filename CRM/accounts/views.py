from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	all_orders = Order.objects.all()

	total = all_orders.count()

	delivered = Order.objects.filter(status = 'Delivered').count()
	pending =all_orders.filter(status = 'Pending').count()

	# dict = {'total':total,'delivered':delivered,'pending':pending}

	return render(request,'accounts/dashboard.html',{'total':total,'delivered':delivered,'pending':pending})

def products(request):
	all_products = Product.objects.all()
	return render(request,'accounts/products.html',{'products':all_products})
def customer(request):
	return render(request,'accounts/customer.html')
