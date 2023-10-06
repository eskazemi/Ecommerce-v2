from django.contrib import admin
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from product.api.views import (
    CategoryViewSet,
    BrandViewSet,
    ProductViewSet,
)
from drf_spectacular.views import (
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularAPIView,
)

router = DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"product", ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
