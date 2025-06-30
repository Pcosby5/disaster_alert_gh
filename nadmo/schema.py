from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Disaster Alert GH API",
      default_version='v1',
      description="API documentation for NADMO Disaster Alert System",
      terms_of_service="https://www.nadmo.gov.gh/terms",
      contact=openapi.Contact(email="support@nadmo.gov.gh"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
