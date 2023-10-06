from rest_framework import serializers
from product.models import (
    AttributeValue,
    Attribute
)


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = (
            "name",
            "id",
        )


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta:
        model = AttributeValue
        fields = (
            "attribute",
            "attribute_value",
        )