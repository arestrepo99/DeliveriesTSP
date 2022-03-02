from django.contrib import admin
from .models import Product, Client, Order, OrderProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderProduct)
