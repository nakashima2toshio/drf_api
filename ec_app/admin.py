from django.contrib import admin
from ec_app.models import Customer, CustomerProfile, Order, Product, Category, ProductCategory

admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductCategory)
