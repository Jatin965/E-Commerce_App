from django.urls import path, include
from .views import ProductList, CategoryViewSet, SellerViewSet, ProductListAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('sellers', SellerViewSet)
router.register('list', ProductList)


app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    path('products-filter/',ProductListAPIView.as_view(), name = 'api-filter'),
    #path('seller/', SellerViewSet, name = 'product-seller'),
    #path('categories/', CategoryViewSet, name = 'product-category'),
]