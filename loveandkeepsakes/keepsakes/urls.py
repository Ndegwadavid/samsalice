from django.urls import path
from . import views

app_name = 'keepsakes'

urlpatterns = [
    path('', views.index, name='index'),
    path('preview/', views.preview, name='preview'),
    path('buy/', views.buy, name='buy'),
]