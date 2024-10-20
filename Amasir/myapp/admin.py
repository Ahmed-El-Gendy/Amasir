from django.contrib import admin
from .models import (Phone, Customer, Product, Category, ShoppingCart, CartItem, Order,
                     OrderItem, Payment, Review, BankAccount)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(BankAccount)
admin.site.register(Phone)
