from django.urls import path

from product import views

urlpatterns = [
    path('ingredients/', views.IngredientsAPI.as_view(), name='ingredients'),
]
