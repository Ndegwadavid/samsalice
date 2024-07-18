from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('category/<str:category>/', views.category_products, name='category_products'),
    path('category/<str:category>/add/', views.add_product, name='add_product'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/toggle-stock/', views.toggle_stock, name='toggle_stock'),
]