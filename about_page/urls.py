from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutus, name='aboutus'),
    path('edit/', views.edit_about_page, name='edit_about_page'),
]
