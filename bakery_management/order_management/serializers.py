from rest_framework import serializers
from order_management.models import Order, OrderDetails
from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        fields = ('__all__',)


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        fields = ('quantity', 'product')


class CreateOrderSerializer(serializers.ModelSerializer):
    products = OrderDetailSerializer(many=True,write_only=True)
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['products', 'product_details' ]

    def get_product_details(self, obj):
        return list(obj.order_detail.values())

    def create(self, validated_data):
        products = validated_data.pop('products')
        instance = super().create(validated_data)

        for product in products:
            OrderDetails.objects.create(order=instance,
                                        product=product['product'],
                                        quantity=product['quantity']
                                    )

        return instance

