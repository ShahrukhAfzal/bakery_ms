from django.urls import path
from order_management import views

urlpatterns = [
    path('order/', views.OrderViewSet, name='order'),
]
