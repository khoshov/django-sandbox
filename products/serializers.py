from django.db.models import F
from rest_framework import serializers

from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        features = instance.features.values_list('feature_type__name', 'value')
        ret.update(dict(features))
        return ret


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
