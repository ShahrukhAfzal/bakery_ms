from rest_framework import serializers
from order_management.models import Order, OrderDetails
from product.serializers import ProductSerializer, IngredientsSerializer


class CreateOrderSerializer(serializers.ModelSerializer):
    product_ids = serializers.ListField()

    class Meta:
        model = Order
        fields = ('id', 'product_ids')

    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids')
        instance = super().create(validated_data)

        for each in product_ids:
            OrderDetails.objects.create(order=instance, product_id=each['id'], quantity=each['quantity'])

        return instance

        # validated_data.update({'customer': self.request.user})

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'products')

    def get_products(self, obj):
        return ProductSerializer(obj.order_detail.all(), many=True).data
