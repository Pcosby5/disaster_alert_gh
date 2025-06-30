from rest_framework import viewsets, permissions
from .models import DisasterReport
from .serializers import DisasterReportSerializer
from .filters import DisasterReportFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from accounts.permissions import CanSubmitReport
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class DisasterReportViewSet(viewsets.ModelViewSet):
    queryset = DisasterReport.objects.all().order_by('-created_at')
    serializer_class = DisasterReportSerializer
    permission_classes = [CanSubmitReport]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DisasterReportFilter
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    @swagger_auto_schema(
    operation_description="Submit a new disaster report",
    request_body=DisasterReportSerializer,
    consumes=['multipart/form-data'],  # 👈 this is the missing part
    responses={
        201: openapi.Response(
            description="Report created successfully",
            schema=DisasterReportSerializer
        ),
        400: 'Bad Request'
    }
)
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().create(request, *args, **kwargs)
        else:
            return super().create(request, *args, **kwargs)
