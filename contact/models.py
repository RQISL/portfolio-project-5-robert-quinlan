from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Categories'

    category = models.ForeignKey('contactus', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField('image')
    name = models.CharField(max_length=254)
    description = models.TextField()
    

    def __str__(self):
        return self.name

