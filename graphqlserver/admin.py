from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import Customer, Device, Product

admin.site.register(Customer)
admin.site.register(Device)
admin.site.register(Product)
