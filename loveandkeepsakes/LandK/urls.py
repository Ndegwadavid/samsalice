from django import views
from django.urls import path
from .views import landk
from . import views

urlpatterns = [
    path('', views.landk, name='landk'),  # Adjust the path as necessary
]
