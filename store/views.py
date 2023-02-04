
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

from .models import *

# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']

    packages = Package.objects.all()
    context = {'packages':packages ,'cartItems':cartItems}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']

    context = {'items':items , 'order':order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        datas=[]
        for i in range(1,cartItems+1):
            datas.append(i)
            

    else:
        items = []
        datas=[]
        order = {'get_cart_total':0, 'get_cart_items':0 }
        cartItems = order['get_cart_items']

    # try:
    #     quantity = OrderItem.objects.all().aggregate(sum('quantity'))['quantity__sum']

    # except OrderItem.DoesNotExist:
    #     quantity = 0



    context = {'items':items , 'order':order,'cartItems':cartItems,'datas':datas}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	packageId = data['packageId']
	action = data['action']
	print('Action:', action)
	print('Package:', packageId)

	customer = request.user.customer
	package = Package.objects.get(id=packageId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(oder=order, package=package)

	if orderItem.quantity == None:
		orderItem.quantity = 0

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
    print('Data:',request.body)
    return JsonResponse('Payment complete!',safe=False)

def view(request, packageId):
    package = Package.objects.get(id=packageId)
    context = {'package': package}
    return render(request, 'store/view.html', context)

def reachus(request):
    context={}
    return render(request, 'store/reachus.html', context)
# def my_view(request):
#     if request.method == 'POST':
#         quantity = request.POST.get('quantity')
#         # do something with the quantity value
#         return render(request, {'quantity': quantity})
def aboutus(request):
    context={}
    return render(request, 'store/aboutus.html', context)

def home(request):
    context={}
    return render(request, 'store/home.html', context)