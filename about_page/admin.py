from django.contrib import admin

from .models import AboutUs

# Register your models here.

class ImageSildeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

    ordering = ('sku',)

class BioPageAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'bio',
    )

admin.site.register(AboutUs, BioPageAdmin)
