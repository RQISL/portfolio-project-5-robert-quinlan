from django.contrib import admin

from .models import AboutUs, BioDetail

# Register your models here.

class ImageSildeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

    ordering = ('sku',)

class BioDetailAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'bio',
    )

admin.site.register(AboutUs, ImageSildeAdmin)
admin.site.register(BioDetail, BioDetailAdmin)