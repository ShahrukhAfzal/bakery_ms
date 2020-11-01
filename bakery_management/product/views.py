from rest_framework import generics

from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product, Ingredients


class IngredientsAPI(generics.CreateAPIView,
                    generics.ListAPIView,):

    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
