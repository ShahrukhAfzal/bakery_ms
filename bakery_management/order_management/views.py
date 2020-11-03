from rest_framework import viewsets
from order_management.models import Order, OrderDetails
from order_management.serializers import  CreateOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('id')
    serializer_class = CreateOrderSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data,
    #                     context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     instance = serializer.save(created_by=self.request.user)

    #     # response_serializer = SurveySerializer(instance=instance, context={'request': request})
    #     return Response(response_serializer.data, status=status.HTTP_201_CREATED)
