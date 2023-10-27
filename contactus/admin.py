from django.contrib import admin
from .models import ContactUs, ContactCategory, FormDynmaic

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'image',
        'name',
        'description',
    )

    ordering = ('sku',)

class ContactCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DynmaicFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'image',
    )

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactCategory, ContactCategoryAdmin)
admin.site.register(FormDynmaic, DynmaicFormAdmin)