from rest_framework import generics, mixins
from order_management.models import Order
from order_management.serializers import  CreateOrderSerializer


class OrderView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                GenericAPIView):
    queryset = Order.objects.order_by('id')
    serializer_class = CreateOrderSerializer
