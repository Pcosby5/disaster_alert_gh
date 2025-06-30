import django_filters
from .models import DisasterReport

class DisasterReportFilter(django_filters.FilterSet):
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = DisasterReport
        fields = ['disaster_type', 'status', 'created_at__gte', 'created_at__lte']
