from django.contrib import admin
from product.models import (
    Product,
    ProductLine,
)


class ProductLineInline(admin.TabularInline):
    model = ProductLine


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
