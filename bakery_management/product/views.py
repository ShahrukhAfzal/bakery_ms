from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.serializers import (ProductSerializer, IngredientsSerializer,
    ProductInventoryUpdateSerializer)
from product.models import Product, Ingredients
from user.permissions import CustomPermission


class IngredientsViewSet(viewsets.ModelViewSet):

    permission_classes = (CustomPermission,)
    queryset = Ingredients.objects.all().order_by('id')
    serializer_class = IngredientsSerializer


class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = (CustomPermission,)
    queryset = Product.objects.all().order_by('-added_on')
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductViewSet, self).get_queryset(*args, **kwargs)
        user = self.request.user

        if user.is_anonymous or not user.is_staff:
            queryset = queryset.filter(is_active=True)

        return queryset

    @action(methods=['POST',], detail=False,
        serializer_class=ProductInventoryUpdateSerializer)
    def update_inventory(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
