from django.db import models
from .attribute import Attribute


class ProductType(models.Model):
    name = models.CharField(max_length=200)
    attribute = models.ManyToManyField(
        Attribute,
        through="ProductTypeAttribute",
        related_name="product_type_attribute"
    )

    def __str__(self):
        return self.name


class ProductTypeAttribute(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="product_type_attribute_at",
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="product_type_attribute_pt"
    )

    class Meta:
        unique_together = ("attribute", "product_type")
