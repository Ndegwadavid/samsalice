from django.urls import path
from .views import RegisterView, LoginView, RegisterTemplateView, LoginTemplateView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('register/', RegisterTemplateView.as_view(), name='register'),
    path('login/', LoginTemplateView.as_view(), name='login'),
]
