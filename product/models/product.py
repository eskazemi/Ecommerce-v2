from django.db import models
from product.models import (
    Brand,
    Category,
)
from mptt.models import TreeForeignKey


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_digital = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="bproduct")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
