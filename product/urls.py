from django.urls import path
from rest_framework import routers

from product import views

router = routers.SimpleRouter()
router.register(r'ingredients', views.IngredientsViewSet, basename='ingredient')
router.register(r'products', views.ProductViewSet, basename='product')


urlpatterns = [
    # path('ingredients/', views.IngredientsAPI.as_view(), name='ingredients'),
]

urlpatterns += router.urls
