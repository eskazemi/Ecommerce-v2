from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        related_name="att_value",
    )

    def __str__(self):
        return f'{self.attribute}-{self.attribute_value}'
