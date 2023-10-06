from django.core.exceptions import ValidationError
from django.db import models
from .product_line import ProductLine
from product.fields import OrderField


class ProductImage(models.Model):
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default='test.jpg')
    product_line = models.ForeignKey(
        ProductLine,
        on_delete=models.CASCADE,
        related_name='product_image',
    )
    order = OrderField(unique_for_field="product_line", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self, exclude=None):
        qs = ProductImage.objects.filter(product_line=self.product_line)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value")

    # for check all clean function and unnecessary call clean in clean test
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.order)
