from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact'),
    path('hireme/<int:id>', views.hireme, name='hireme'),
    path('add_category', views.add_contact_category, name='add_category'),
    path('edit/<int:contact_id>/', views.edit_contact_category, name='edit_category'),
    path('delete/<int:contact_id>/', views.delete_contact_category, name='delete_category'),
]