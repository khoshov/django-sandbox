from django.db.models import F, OuterRef, Prefetch, Subquery
from rest_framework import viewsets

from products.models import Category, Product, ProductFeature, \
    ProductFeatureType
from products.serializers import (
    CategorySerializer,
    ProductReadSerializer,
    ProductWriteSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    #
    # queryset = Product.objects.all().select_related(
    #     'category',
    # ).prefetch_related(
    #     'features',
    # ).prefetch_related(
    #     'features__feature_type',
    # ).annotate(
    #     feature_type_name=F('features__feature_type__name')
    # )

    # queryset =

    def get_queryset(self):
        return Product.objects.all().select_related(
            'category',
        ).prefetch_related(
            'features',
            'features__feature_type',
        )

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProductReadSerializer
        return ProductWriteSerializer
