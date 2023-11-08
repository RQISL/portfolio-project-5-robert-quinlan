from django.contrib import admin
from .models import Product, Category, CategoriesGroups

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'image',
        'name',
        'description',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoriesGroups, CategoryGroupAdmin)