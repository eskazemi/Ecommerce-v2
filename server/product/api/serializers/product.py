from rest_framework import serializers
from product.models import (
    Product,
    ProductLine,
    Attribute
)
from .image import ProductImageSerializer
from .attribute import (
    AttributeValueSerializer,
    AttributeSerializer,
)


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("attribute_value")
        attr_value = {}
        for key in av_data:
            attr_value.update({key["attribute"]["id"]: key["attribute_value"]})
        data.update({"specification": attr_value})
        return data


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)
    attribute = serializers.SerializerMethodField(method_name='get_attribute')

    class Meta:
        model = Product
        # exclude = ("id",)
        fields = (
            "name",
            "slug",
            "description",
            "product_line",
            "category_name",
            "brand_name",
            "attribute"
        )
    def get_attribute(self, obj):
        attribute = Attribute.objects.filter(product_type_attribute__product__id=obj.id)
        return AttributeSerializer(attribute, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("attribute")
        attr_value = {}
        for key in av_data:
            attr_value.update({key["id"]: key["name"]})
        data.update({"type specification": attr_value})
        return data
