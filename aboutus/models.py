from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class ImageSlides(models.Model):
    number = models.IntegerField()
    image = CloudinaryField('image')
    name = models.CharField(max_length=254)
    
    
    def __str__(self):
        return self.name