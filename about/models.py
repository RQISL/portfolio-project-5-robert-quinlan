from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class AboutUs(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.name


class BioDetail(models.Model):
    title = models.CharField(max_length=254)
    bio = models.TextField()

    def __str__(self):
        return self.title
