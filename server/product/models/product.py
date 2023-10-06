from django.db import models
from .brand import Brand
from mptt.models import TreeForeignKey
from .product_type import ProductType


# class ActiveManager(models.Manager):
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(is_active=True)
#     def isactive(self):
#         return self.get_queryset().filter(is_active=True)

class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Product(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
    )
    category = TreeForeignKey("Category",
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name="bproduct")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    is_digital = models.BooleanField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ActiveQueryset.as_manager()

    # isactive = ActiveManager()

    def __str__(self):
        return self.name
