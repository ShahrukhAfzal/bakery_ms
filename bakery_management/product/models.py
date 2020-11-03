from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)
    cost_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    ingredients = models.ManyToManyField('Ingredients',
        through='ProductIngredient',related_name='product_ingredients')
    is_active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} = ${}".format(self.name, self.selling_price)


class Ingredients(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, related_name='products',
                on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, related_name='products',
                on_delete=models.SET_NULL, blank=True, null=True)
    quantity_percent = models.FloatField(default=0)
