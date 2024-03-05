from django.contrib import admin
from libadmin.models import reg

# Register your models here.
class regAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    #list_display= __all__
    search_fields=['name']
admin.site.register(reg,regAdmin)

