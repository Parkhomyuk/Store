from django.contrib import admin
from .models import Product, Brand, Subcategory, Category

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Subcategory)
admin.site.register(Category)