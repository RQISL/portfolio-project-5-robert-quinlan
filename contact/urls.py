from django.urls import path
from contact.views import (Contact, Thank_You)
urlpatterns = [
    path("", Contact.as_view(), name="contact"),
    path('thankyou/', Thank_You.as_view(), name='thankyou'),
]
