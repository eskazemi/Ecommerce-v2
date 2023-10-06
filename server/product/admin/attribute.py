from django.contrib import admin
from product.models import (
    Attribute,
    AttributeValue,
)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = (
        "attribute_value",
        "attribute",
    )
