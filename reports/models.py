import uuid
from django.db import models  # ✅ no GeoDjango now
from accounts.models import User


class DisasterReport(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('fake', 'Fake'),
    )

    TYPE_CHOICES = (
        ('fire', 'Fire'),
        ('flood', 'Flood'),
        ('accident', 'Accident'),
        ('other', 'Other'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporter = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='reports')
    disaster_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='disaster_photos/', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.disaster_type} - {self.status} ({self.created_at.date()})"
