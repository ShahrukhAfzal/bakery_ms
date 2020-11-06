from django.urls import path
from rest_framework import routers

from product import views

router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientsViewSet)
router.register(r'products', views.ProductViewSet)


urlpatterns = [
    # path('ingredients/', views.IngredientsAPI.as_view(), name='ingredients'),
]

urlpatterns += router.urls
