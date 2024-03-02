from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class AboutUs(models.Model):

    class Meta:
        verbose_name_plural = 'About us'

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    bio = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name
