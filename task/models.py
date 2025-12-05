from django.db import models
from django.conf import settings
from .enums import EventType, Priority, ComplianceType

# Create your models here.
class TaskTemplate(models.Model):
    title = models.CharField(max_length=255)
    default_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title




class Event(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events"
    )

    template = models.ForeignKey(
        TaskTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=255)
    date = models.DateTimeField()

    event_type = models.CharField(max_length=20, choices=EventType.choices)
    priority = models.CharField(max_length=20, choices=Priority.choices)

    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    recurring = models.CharField(max_length=100, null=True, blank=True)

    compliance_type = models.CharField(
        max_length=50,
        choices=ComplianceType.choices,
        default=ComplianceType.NONE
    )

    requires_trade = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
