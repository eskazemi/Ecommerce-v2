from rest_framework import serializers
from product.models import (
    Product,
    ProductLine,
)
from .image import ProductImageSerializer
from .attribute import AttributeValueSerializer


class ProductLineSerializer(serializers.ModelSerializer):
    # backward relation
    product_image = ProductImageSerializer(many=True)
    attribute_value = AttributeValueSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = (
            "price",
            "sku",
            "stock_qty",
            'order',
            'product_image',
            'attribute_value',

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
