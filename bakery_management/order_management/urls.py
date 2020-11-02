from django.urls import path
from rest_framework import routers

from order_management import views

router = routers.DefaultRouter()

urlpatterns = [
    # path('ingredients/', views.IngredientsAPI.as_view(), name='ingredients'),
]

urlpatterns += router.urls
