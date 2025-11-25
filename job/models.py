from django.db import models
from .enums import ServiceTypeChoices, PriorityChoices
from django.core.validators import MinValueValidator

class QuoteRequest(models.Model):
    service_required = models.CharField(
        max_length=20,
        choices=ServiceTypeChoices.choices,
        null=False,
        blank=False
    )
    location = models.CharField(max_length=255, null=False, blank=False)
    budget_range = models.CharField(max_length=50, null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.MEDIUM
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_required} - {self.location} - {self.priority}"
