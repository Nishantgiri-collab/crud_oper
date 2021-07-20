from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','Date','Name_of_product','Price','Quality','Amount','Stock']
admin.site.register(Product,ProductAdmin)
