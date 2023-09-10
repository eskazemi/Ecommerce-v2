from rest_framework import viewsets
from product.models import Brand
from product.api.serializers import BrandSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class BrandViewSet(viewsets.ViewSet):
    """

    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(instance=self.queryset, many=True)
        return Response(serializer.data)
