from django.contrib import admin
from .models import Product, Goodie

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')  # Ajoutez 'category' à la liste d'affichage

class GoodieAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')  # Ajoutez 'category' à la liste d'affichage

admin.site.register(Product, ProductAdmin)
admin.site.register(Goodie, GoodieAdmin)
