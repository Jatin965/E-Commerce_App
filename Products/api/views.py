from rest_framework import generics, viewsets, mixins, views, status, exceptions
from .serializers import ProductAllInfoSerializer, ProductSerializer, SellerSerializer, CategorySerializer
from Products.models import Category, Seller, Product
from rest_framework.response import Response


class ProductList(viewsets.ModelViewSet):
    serializer_class = ProductAllInfoSerializer
    queryset = Product.objects.all()



class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_fields = (
        'category_id',
    )

    search_fields = (
        'title',
    )



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    



def get(self, request):
        products = Product.objects.all()
        serializer = ProductAllInfoSerializer(products, many = True)
        return Response(serializer.data)


def post(self, request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def perform_create(self, serializer):
        serializer.save(user = self.request.user)


def post(self, request, *args, **kwargs):
    serializer_class = ProductSerializer
    return self.create(request, *args, **kwargs)