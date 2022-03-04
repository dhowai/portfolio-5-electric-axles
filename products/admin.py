from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin for category model
    """
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin for product model
    """
    list_display = ['name', 'slug', 'category', 'price',
                    'in_stock', 'created', 'updated']
    list_filter = ['category', 'in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}