from django.contrib import admin

from .models import HomePage

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
    
admin.site.register(HomePage, ImageUploadAdmin)

