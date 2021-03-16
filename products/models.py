from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ProductFeatureType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class ProductFeature(models.Model):
    product = models.ForeignKey(
        Product,
        models.CASCADE,
        related_name='features',
    )
    feature_type = models.ForeignKey(ProductFeatureType, models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.product.name} {self.feature_type}: {self.value}'
