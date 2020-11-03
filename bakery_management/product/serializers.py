from rest_framework import serializers

from product.models import Product, Ingredients, ProductIngredient


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'description')


class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductIngredient
        fields = ('ingredient', 'quantity_percent')


class ProductSerializer(serializers.ModelSerializer):

    ingredients_details = ProductIngredientSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'cost_price', 'selling_price',
                    'quantity', 'ingredients_details'
                )

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients_details')
        instance = super().create(validated_data)

        for ingredient in ingredients:
            ProductIngredient.objects.create(
                ingredient=ingredient['ingredient'],product=instance,
                quantity_percent=ingredient['quantity_percent'])

        return instance
