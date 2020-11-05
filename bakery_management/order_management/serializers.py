from rest_framework import serializers
from order_management.models import Order, OrderDetails
from product.serializers import ProductSerializer, IngredientsSerializer
from product.models import Product


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetails
        fields = ('quantity', 'product')


class CreateOrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, write_only=True)
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'products', 'product_details' ]

    def get_product_details(self, obj):
        return list(obj.order_detail.values())

    def create(self, validated_data):
        products = validated_data.pop('products')
        instance = super().create(validated_data)

        order_list = list()
        for product in products:
            quantity = product['quantity']
            product_obj = product['product']

            #finding total price for a product
            ordered_price = (product_obj.selling_price) * quantity

            order_list.append(OrderDetails(order=instance,
                                        product=product_obj,
                                        quantity=quantity,
                                        ordered_price=ordered_price
                                        )
                                    )
            product_obj.available_quantity = product_obj.available_quantity - quantity
            product_obj.save()

        OrderDetails.objects.bulk_create(order_list)

        return instance


    def validate_products(self, products):

        for product in products:
            product_obj = product['product']
            available_quantity = product_obj.available_quantity
            quantity_to_buy = product['quantity']
            product_name = product_obj.name
            if (available_quantity < quantity_to_buy):
                    error = "Only {} Products are available for {}".format(
                                available_quantity, product_name)
                    raise serializers.ValidationError(error)

            if not product_obj.is_active:
                error = "{} is not available.".format(product_name)
                raise serializers.ValidationError(error)


        return products
