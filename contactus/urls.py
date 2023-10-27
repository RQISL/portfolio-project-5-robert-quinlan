from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contactus'),
    path('hireme/<int:id>', views.hireme, name='hireme'),
]
