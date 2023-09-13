from rest_framework import serializers
from product.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)
