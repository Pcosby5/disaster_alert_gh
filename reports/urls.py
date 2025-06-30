from rest_framework.routers import DefaultRouter
from .views import DisasterReportViewSet

router = DefaultRouter()
router.register(r'reports', DisasterReportViewSet, basename='reports')

urlpatterns = router.urls
