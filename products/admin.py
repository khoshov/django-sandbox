from django.contrib import admin

from products.models import (
    Category,
    Product,
    ProductFeature,
    ProductFeatureType,
)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductFeature)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductFeatureType)
class ProductAdmin(admin.ModelAdmin):
    pass
