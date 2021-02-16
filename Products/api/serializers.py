from rest_framework import serializers
from Products.models import Category, Seller, Product


class CategorySerializer(serializers.ModelSerializer):
    random_photo = serializers.SerializerMethodField()

    def get_random_photo(self, obj):
        try:
            return obj.products.first().photo
        except:
            return ''

    class Meta:
        model = Category
        fields = [
            'id', 
            'name', 
            'random_photo',
        ]



class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            'id', 
            'name',
        ]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'photo',
            'price', 
            'title',
            'category', 
            'seller',
            'photo',
        ]



class ProductAllInfoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()
    class Meta:
        model = Product
        fields = [
            'id', 
            'photo',
            'price', 
            'title',
            'category', 
            'seller',
            'photo',
        ]