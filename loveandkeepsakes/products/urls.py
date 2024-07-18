from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:category>/', views.category_products, name='category_products'),
]