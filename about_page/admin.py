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
    list_display = (
        'sku',
        'name',
        'title',
        'bio',
        'image',
    )


admin.site.register(AboutUs, BioPageAdmin)
