from django.urls import path
from rest_framework import routers

from product import views

router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientsViewSet)


urlpatterns = [
    # path('ingredients/', views.IngredientsAPI.as_view(), name='ingredients'),
]

urlpatterns += router.urls
