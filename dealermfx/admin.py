from django.contrib import admin
from .models import table_vehicles

# Register your models here.
class vehicles_admin_show(admin.ModelAdmin): 
    list_display = ('id', 'name', 'model', 'year', 'rent', 'user', 'rented')


admin.site.register(table_vehicles, vehicles_admin_show)
