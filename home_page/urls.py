from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('edit/', views.edit_home_page, name='edit_home_page'),
]