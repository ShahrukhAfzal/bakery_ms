from rest_framework import generics, mixins, viewsets
from order_management.models import Order
from order_management.serializers import  CreateOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('id')
    serializer_class = CreateOrderSerializer
