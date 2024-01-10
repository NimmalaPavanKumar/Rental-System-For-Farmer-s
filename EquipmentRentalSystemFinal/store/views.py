from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cookieCart, cartData, guestOrder

# Create your views here.

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
        
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context )

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items , 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context )

def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items , 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context )

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)
    
def Aboutus(request):
    return render(request,'store/aboutus.html', {})
    
def Services(request):
    return render(request,'store/services.html', {})

def Contactus(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     ins = Contact(name=name, email=email, message=message)
    #     ins.save()
    #     print("ok")   
    return render(request,'store/contactus.html', {})

def Feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ins = Feedbacks(name=name, email=email, message=message)
        ins.save()
        print("ok")   
    return render(request,'store/feedback.html', {})

def Index(request):
    return render(request,'store/index.html', {})

def Supplierdet(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        
        ins = Supplier(first_name=first_name, lastname=lastname, gender=gender, date_of_birth=date_of_birth, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, address=address)
        ins.save()
        print("ok")
        return redirect('product')
    return render(request,'store/supplier.html', {})

from django.shortcuts import render
from .models import Product

def Productdet(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        name = request.POST.get('name')
        price = request.POST.get('price')
        digital = request.POST.get('digital')
        
        # Check if 'image' key exists in request.FILES
        image = request.FILES.get('image')

        if image:
            ins = Product(name=name, price=price, digital=digital, image=image)
            ins.save()
            print("ok")
        else:
            print("Image not found in request.FILES")

    return render(request, 'store/product.html', {})


