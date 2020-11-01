from django.urls import path

from user import views

urlpatterns = [
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
]
