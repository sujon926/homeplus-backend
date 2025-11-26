from rest_framework import serializers
from .models import QuoteRequest
from .enums import ServiceTypeChoices, PriorityChoices
# job/serializers.py
from rest_framework import serializers
from .models import QuoteBid, QuoteRequest
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

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



class QuoteBidSerializer(serializers.ModelSerializer):
    worker = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = QuoteBid
        fields = ['id', 'quote', 'worker', 'proposed_value', 'availability_date', 'note', 'status', 'created_at']
        read_only_fields = ['worker', 'status', 'created_at']

    def validate_availability_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Availability date must be in the future.")
        return value




class QuoteBidStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteBid
        fields = ['status']

    def validate_status(self, value):
        if value not in ["ACCEPTED", "REJECTED"]:
            raise serializers.ValidationError("Status must be ACCEPTED or REJECTED.")
        return value
