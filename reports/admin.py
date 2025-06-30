from django.contrib import admin
from .models import DisasterReport

@admin.register(DisasterReport)
class DisasterReportAdmin(admin.ModelAdmin):
    list_display = ('disaster_type', 'status', 'created_at')
    list_filter = ('disaster_type', 'status', 'created_at')
