from rest_framework import serializers
from product.models import Product
from .brand import BrandSerializer
from .category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
