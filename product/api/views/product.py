from rest_framework import viewsets
from product.models import Product
from product.api.serializers import ProductSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class ProductViewSet(viewsets.ViewSet):
    """

    """
    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
