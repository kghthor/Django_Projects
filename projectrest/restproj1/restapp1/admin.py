
from django.contrib import admin
# Register your models here.
from .models import Product
class productAdmin(admin.ModelAdmin):
    list_display=['id','name','stars']
    ordering=['id',]
admin.site.register(Product,productAdmin)