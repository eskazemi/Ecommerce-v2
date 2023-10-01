from .base import INSTALLED_APPS

# ###########
# Third-party apps #
#############

INSTALLED_APPS.append("rest_framework")
INSTALLED_APPS.append('drf_spectacular')

# ##########
# local apps
# ##########

INSTALLED_APPS.append("product")

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'ecommerce-v2',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}