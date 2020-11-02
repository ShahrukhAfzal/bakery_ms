from rest_framework import serializers

from product.models import Product, Ingredients


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'cost_price', 'selling_price',
                    'quantity'
                )


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'description')

