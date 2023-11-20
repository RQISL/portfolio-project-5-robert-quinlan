from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class HomePage(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    head = models.CharField(max_length=254)
    info = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.title


class ExhibationView(models.Model):
    name = models.CharField(max_length=254)
    info = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
