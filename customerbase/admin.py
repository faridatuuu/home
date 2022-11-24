from django.contrib import admin
from . models import Customer, Cart

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_displahy = ['id', 'user', 'first_name', 'last_name', 'email', 'phone']

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'price','paid', 'amount']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'paid', 'amount', 'purchase_date']   

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
