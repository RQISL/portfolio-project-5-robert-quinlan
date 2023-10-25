from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'image',
        'name',
        'description',
    )

    ordering = ('sku',)

admin.site.register(ContactUs, ContactUsAdmin)