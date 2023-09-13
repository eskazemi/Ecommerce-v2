from rest_framework import serializers
from product.models import (
    Product,
    ProductLine,
)
from .brand import BrandSerializer
from .category import CategorySerializer


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = (
            "id",
            "product",
            "is_active",
        )


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        # exclude = ("id",)
        fields = (
            "name",
            "slug",
            "description",
            "product_line",
            "category_name",
            "brand_name"
        )



