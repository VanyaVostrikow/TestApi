from django.contrib import admin
from testapi.models import Product, GroupsofProducts, CategoriesOfProducts
# Register your models here.

admin.site.register(Product)
admin.site.register(GroupsofProducts)
admin.site.register(CategoriesOfProducts)