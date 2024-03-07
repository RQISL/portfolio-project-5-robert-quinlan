from django.db import models


class ContactView(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.email
