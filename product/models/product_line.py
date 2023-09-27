from django.db import models
from .product import Product
from .attribute import AttributeValue
from product.fields import OrderField
from django.core.exceptions import ValidationError
from .product_type import ProductType


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2,
                                max_digits=5)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="product_line")
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="product",
                       blank=True)
    attribute_value = models.ManyToManyField(
        AttributeValue,
        related_name="product_line_attribute_value",
        through="ProductLineAttributeValue")
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self, exclude=None):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")

    # for check all clean function and unnecessary call clean in clean test
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE,
        related_name="product_attribute_value_av",
    )
    product_line = models.ForeignKey(
        ProductLine,
        on_delete=models.CASCADE,
        related_name="product_attribute_line_pl"
    )

    class Meta:
        unique_together = ("attribute_value", "product_line")
