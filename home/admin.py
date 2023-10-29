from django.contrib import admin

from .models import HomePage, ElenaInfo

# Register your models here.

class ImageUploadAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

class ElenaInfoAdmin(admin.ModelAdmin):
    list_display = (
        'head',
        'info',
    )

admin.site.register(HomePage, ImageUploadAdmin)
admin.site.register(ElenaInfo, ElenaInfoAdmin)