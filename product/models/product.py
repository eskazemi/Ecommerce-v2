from django.db import models
from product.models import (
    Brand,
    Category,
)
from mptt.models import TreeForeignKey


# class ActiveManager(models.Manager):
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(is_active=True)
#     def isactive(self):
#         return self.get_queryset().filter(is_active=True)

class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    is_digital = models.BooleanField()
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name="bproduct")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = TreeForeignKey("Category",
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()
    # isactive = ActiveManager()

    def __str__(self):
        return self.name
