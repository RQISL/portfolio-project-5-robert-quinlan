from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('category_paintings', views.category_paintings, name='category_paintings'),
    path('<product_id>', views.product_detail, name='product_detail'),
]