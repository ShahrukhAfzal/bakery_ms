from rest_framework import generics
from rest_framework import viewsets

from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product, Ingredients


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
