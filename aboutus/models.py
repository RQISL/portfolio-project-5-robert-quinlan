from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class AboutPersonal(models.Model):
    number = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField('image')
    name = models.CharField(max_length=254)
    
    
    def __str__(self):
        return self.name