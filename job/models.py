from django.db import models
from .enums import ServiceTypeChoices, PriorityChoices
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from common.models import TimeStampedModel


User = get_user_model()



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


 
class QuoteBid(TimeStampedModel):
    quote = models.ForeignKey(
        'QuoteRequest',
        on_delete=models.CASCADE,
        related_name='bids'
    )
    trader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='trader_bids'
    )
    proposed_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        null=True,
        blank=True
    )
    availability_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date worker can start the job"
    )
    note = models.TextField(
        null=True,
        blank=True,
        help_text="Worker additional message (optional)"
    )

    def __str__(self):
        return f"Bid by {self.trader.email} for Quote #{self.quote.id}"
