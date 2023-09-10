from rest_framework import viewsets
from product.models import Category
from product.api.serializers import CategorySerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class CategoryViewSet(viewsets.ViewSet):
    """

    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
