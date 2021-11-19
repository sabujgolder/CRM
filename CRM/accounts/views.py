from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
	all_orders = Order.objects.all()
	all_customers = Customer.objects.all()



	total = all_orders.count()

	delivered = Order.objects.filter(status = 'Delivered').count()
	pending =all_orders.filter(status = 'Pending').count()

	dict = {'total':total,'delivered':delivered,'orders':all_orders,
			'pending':pending,'customers':all_customers}

	return render(request,'accounts/dashboard.html',context=dict)

def products(request):
	all_products = Product.objects.all()
	return render(request,'accounts/products.html',{'products':all_products})

def customer(request,pk):

	customer_data = Customer.objects.get(id=pk)

	customer_orders = customer_data.order_set.all()
	total_orders = customer_orders.count()
	dict = {'customer_data':customer_data,'customer_orders':customer_orders,'total_orders':total_orders}
	return render(request,'accounts/customer.html',context = dict)

def create_order(request):

	create_form = order_form()

	if request.method == "POST":
		create_form = order_form(request.POST)

		if form.is_valid():
			form.save()
			return redirect('')
	dict = {'form':create_form}

	return render(request,'accounts/create_order.html',context=dict)
