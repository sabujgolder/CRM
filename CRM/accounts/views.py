from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from .forms import order_form,customer_form
from django.urls import reverse
from django.forms import inlineformset_factory
from .filters import *

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
	# order_products = customer_orders.product

	# all_products=[]
	# for order in customer_orders:
	# 	all_products.append(order.product.name)

	total_orders = customer_orders.count()

	filter_orders = OrderFilter(request.GET,queryset=customer_orders)
	customer_orders = filter_orders.qs

	dict = {'customer_data':customer_data,'customer_orders':customer_orders,
	'total_orders':total_orders,'filter_orders':filter_orders}
	return render(request,'accounts/customer.html',context = dict)

def create_order(request):

	data_form = order_form()
	orders = Order.objects.all()
	last_fiver_orders = orders[:5]
	if request.method == "POST":
		data_form = order_form(request.POST)

		if data_form.is_valid():
			data_form.save()
			return redirect('/')
	dict = {'form':data_form,'orders':last_fiver_orders}

	return render(request,'accounts/create_order.html',context=dict)

def create_bulk_order(request,pk):

	OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))

	customer = Customer.objects.get(id=pk)

	formset = OrderFormSet(instance=customer)
	# data_form = order_form(initial={'customer':customer})
	orders = Order.objects.all()
	last_fiver_orders = orders[:5]
	if request.method == "POST":
		formset = OrderFormSet(request.POST,instance=customer)

		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('create_bulk_order', kwargs={'pk':pk}))

	dict = {'formset':formset,'orders':last_fiver_orders}

	return render(request,'accounts/create_order.html',context=dict)


def create_customer(request):

	customer = Customer.objects.all()
	customer_creation_form = customer_form()

	if request.method == "POST":
		customer_creation_form = customer_form(request.POST)

		if customer_creation_form.is_valid():
			customer_creation_form.save()
			return redirect('/')
	dict = {'form':customer_creation_form,'customers':customer}
	return render(request,'accounts/create_customer.html',context=dict)

def delete_order(request,pk):

	order = Order.objects.get(id=pk)
	order.delete()
	return redirect('/')

def update_order(request,pk):

	order = Order.objects.get(id=pk)
	data_form = order_form(instance=order)

	if request.method == "POST":
		data_form = order_form(request.POST,instance=order)
		if data_form.is_valid():
			data_form.save()
			return redirect('/')
	dict = {'form':data_form}
	return render(request,'accounts/update_order.html',context=dict)

def update_customer(request,pk):
	customer = Customer.objects.get(id=pk)
	customer_update_form = customer_form(instance=customer)

	if request.method == "POST":
		customer_update_form = customer_form(request.POST,request.FILES,instance=customer)

		if customer_update_form.is_valid():
			customer_update_form.save()
			return redirect('/')
	dict = {'form':customer_update_form,'customer':customer}
	return render(request,'accounts/update_customer.html',context=dict)
