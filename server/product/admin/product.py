from django.contrib import admin
from product.models import (
    Product,
    ProductLine,
    ProductImage,
    AttributeValue,
    ProductType,
    Attribute
)
from django.urls import reverse
from django.utils.safestring import mark_safe


class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk]
        )
        if instance.pk:
            link = mark_safe('<a href="{u}">edit<a/>'.format(u=url))
            return link
        else:
            return ""


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue.product_line_attribute_value.through


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        AttributeValueInline
        ]


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    list_display = (
        "name",
        "brand",
        "category",
        'is_digital',
        'is_active',
    )
    prepopulated_fields = {"slug": ('description',)}


class AttributeInline(admin.TabularInline):
    model = Attribute.product_type_attribute.through


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [AttributeInline]
    list_display = ("name",)


