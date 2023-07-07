
from django.contrib import admin
from cars.models import Car, Brand #CarInventory

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

"""
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'cars_count')
 """


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
""" admin.site.register(CarInventory, CarInventoryAdmin) """
