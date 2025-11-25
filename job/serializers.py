from rest_framework import serializers
from .models import QuoteRequest
from .enums import ServiceTypeChoices, PriorityChoices

class QuoteRequestSerializer(serializers.ModelSerializer):
    service_required = serializers.ChoiceField(choices=ServiceTypeChoices.choices)
    priority = serializers.ChoiceField(choices=PriorityChoices.choices)

    class Meta:
        model = QuoteRequest
        fields = ['id', 'service_required', 'location', 'budget_range', 'priority', 'created_at']

    def validate_location(self, value):
        if not value.strip():
            raise serializers.ValidationError("Location cannot be empty")
        return value
