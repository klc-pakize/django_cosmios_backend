from django.contrib import admin

from .models import Address, Product, Profile

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
