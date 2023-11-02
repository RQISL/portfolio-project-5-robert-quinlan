from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.

class ContactCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Groups'
     
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Categories'

    category = models.ForeignKey('ContactCategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField('image')
    name = models.CharField(max_length=254)
    description = models.TextField()
    

    def __str__(self):
        return self.name

class FormDynmaic(models.Model):
    class Meta:
        verbose_name_plural = 'Category form'

    category = models.ForeignKey('ContactCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
   

    def __str__(self):
        return self.name