from rest_framework import viewsets

from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product, Ingredients


class IngredientsViewSet(viewsets.ModelViewSet):

    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('-added_on')
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductViewSet, self).get_queryset(*args, **kwargs)

        if user.is_anonymous or not user.is_staff:
            queryset = queryset.filter(is_active=True)

        return queryset
