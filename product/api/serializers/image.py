from rest_framework import serializers
from product.models import (
    ProductImage,
)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = (
            "id",
            "product_line",
        )
