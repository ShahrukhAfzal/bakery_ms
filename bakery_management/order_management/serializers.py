from rest_framework import serializers
from order_management.models import Order, OrderDetails
from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        fields = ('__all__',)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'quantity')


class CreateOrderSerializer(serializers.ModelSerializer):
    products = OrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'products')

    def create(self, validated_data):
        products = validated_data.pop('products')
        instance = super().create(validated_data)

        for each in products:
            OrderDetails.objects.create(order=instance, product_id=each['id'], quantity=each['quantity'])

        return instance

