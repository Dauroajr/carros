from django import forms
from django.contrib import admin
from django.db import models

from cars.models import Car, Brand, CarInventory


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

    formfield_overrides = {
        models.DecimalField: {
            'widget': forms.TextInput(attrs={'step': '0,01'})
        }
    }


class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'cars_count')

    formfield_overrides = {
        models.DecimalField: {
            'widget': forms.TextInput(attrs={'step': '0,01'})
        }
    }



admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)
