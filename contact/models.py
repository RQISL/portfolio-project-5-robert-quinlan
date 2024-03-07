from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = "Contact Categories"

    category = models.ForeignKey(
        "contactus", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = CloudinaryField("image")
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class ContactView(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.first_name
