import re
from django.shortcuts import render, redirect
from django.core import serializers
from .forms import Add_Client, Add_Order, OrderProductFormSet, Add_Product
from .models import Product, Client, Order
import os

def add_order(request):
    if request.method == "POST":
        data = request.POST
        order = Add_Order(data)
        orderProductFormSet = OrderProductFormSet(data)
        print(order)
        if order.is_valid() and orderProductFormSet.is_valid():
            order_object = order.save()
            for orderProduct in orderProductFormSet:
                if orderProduct.is_valid():
                    to_save = orderProduct.save(commit=False)
                    to_save.order = order_object
                    to_save.save()
    return render(request, "store/add_order.html", 
        {"Add_Order": Add_Order, "OrderProductFormSet" : OrderProductFormSet, 
            'MapsJavaScirptAPIKey' : os.environ['MapsJavaScirptAPIKey']})

def dashboard(request):
    if request.method == "POST":
        form = Add_Product(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
    return render(request, "store/dashboard.html", 
        {"form": Add_Product,"products": Product.objects.all()})

def processManageRequest(request,model,add_form, add = True):
    if request.method == "POST":
        if 'remove' in request.POST:
            model.objects.get(id=int(request.POST['remove'])).delete()
        else:
            if add:
                form = add_form(request.POST)
                if form.is_valid():
                    form.save()
    return render(request, "store/manage.html", 
        {"form": add_form,"model": model.objects.all(), "name": model.__name__} )

def edit_products(request):
    return processManageRequest(request,Product,Add_Product)

def edit_clients(request):
    return processManageRequest(request,Client,Add_Client)

def edit_orders(request):
    return processManageRequest(request,Order,None,add=False)