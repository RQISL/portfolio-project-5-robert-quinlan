from django.contrib import admin

from .models import ImageSlides

# Register your models here.

class ImageSildeAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'image',
        'name',
    )

    ordering = ('number',)

admin.site.register(ImageSlides, ImageSildeAdmin)