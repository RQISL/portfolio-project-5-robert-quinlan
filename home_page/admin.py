from django.contrib import admin

from .models import HomePage, ExhibationView

# Register your models here.

class ImageUploadAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
        'head',
        'info',
    )
    
    ordering = ('sku',)

class ExhibationUploadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'info',
    )
    
admin.site.register(HomePage, ImageUploadAdmin)
admin.site.register(ExhibationView, ExhibationUploadAdmin)

