from rest_framework import routers

from products.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, 'Category')
router.register(r'products', ProductViewSet, 'Product')
