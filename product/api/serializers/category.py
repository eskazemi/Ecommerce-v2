from rest_framework import serializers
from product.models import Category


class CategorySerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='name')

    class Meta:
        model = Category
        exclude = ("id",)
        # fields = ("category_name",)
