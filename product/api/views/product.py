from rest_framework import viewsets
from product.models import Product
from product.api.serializers import ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from django.db import connection
from utils import logging_queries


class ProductViewSet(viewsets.ViewSet):
    """

    """
    queryset = Product.objects.all().isactive()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(instance=
                                       self.queryset.filter(slug=slug).select_related(
                                           "category", "brand"), many=True)
        data = Response(serializer.data)
        q = list(connection.queries)
        logging_queries(q)
        return data

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)",
        url_name="all"
    )
    def list_product_by_category_slug(self, request, slug=None):
        """
            Args:
                ...
            Return:
                ...
            Example:
                ...
        """
        serializer = ProductSerializer(
            instance=self.queryset.filter(category__slug=slug), many=True)
        return Response(serializer.data)
