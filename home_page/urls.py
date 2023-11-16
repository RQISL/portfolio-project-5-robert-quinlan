from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('edit/', views.edit_home_page, name='edit_home_page'),
    path('exhibation/', views.exhibation, name='exhibations'),
    path('add_exhibation/', views.add_exhibation, name='add_exhibations'),
]