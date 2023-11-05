from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class HomePage(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    image = CloudinaryField('image')
    head = models.CharField(max_length=254)
    info = models.TextField()
    
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    