from django.contrib import admin

# Register your models here.
from .models import Product, Colour, Customer, Category, SubCategory, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(Colour)

