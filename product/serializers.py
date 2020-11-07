from rest_framework import serializers

from product.models import (Product, Ingredients, ProductIngredient,
    ProductInventoryDetail)


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'description')


class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredient_detail = serializers.SerializerMethodField()

    class Meta:
        model = ProductIngredient
        fields = ('ingredient', 'ingredient_detail', 'quantity_percent')

        def get_fields(self, *args, **kwargs):
            fields = super().get_fields(*args, **kwargs)
            user = self.context.get('request').user

            if not user.is_staff:
                restricted_fields = ('id',)

                for field in restricted_fields:
                    fields.pop(field)

            return fields

    def get_ingredient_detail(self, obj):
        return IngredientsSerializer(obj.ingredient).data


class ProductSerializer(serializers.ModelSerializer):

    ingredients_details = ProductIngredientSerializer(many=True, required=False)
    ingredients = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'cost_price', 'selling_price',
                    'available_quantity', 'ingredients_details', 'ingredients'
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredients_details'].context.update(self.context)

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        user = self.context.get('request').user

        if not user.is_staff:
            restricted_fields = ('cost_price', 'id', 'available_quantity')

            for field in restricted_fields:
                fields.pop(field)

        return fields

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients_details', [])
        instance = super().create(validated_data)

        for ingredient in ingredients:
            ProductIngredient.objects.create(
                ingredient=ingredient.get('ingredient'),
                product=instance,
                quantity_percent=ingredient.get('quantity_percent'))

        return instance

    def get_ingredients(self, obj):

        return ProductIngredientSerializer(obj.products.all(), many=True).data


class ProductInventoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInventoryDetail
        fields = ('product', 'quantity_added')

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data.update({'added_by': user})
        instance = super().create(validated_data)

        product = validated_data.get('product')
        product.available_quantity += validated_data.get('quantity_added', 0)
        product.save()

        return instance
