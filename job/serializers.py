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
    quote_id = serializers.IntegerField(write_only=True)  # send only ID
    trader_id = serializers.IntegerField(write_only=True)  # send only ID

    class Meta:
        model = QuoteBid
        fields = [
            "id",
            "quote_id",
            "trader_id",
            "proposed_value",
            "availability_date",
            "note",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, attrs):
        # Validate quote exists
        try:
            quote = QuoteRequest.objects.get(id=attrs["quote_id"])
        except QuoteRequest.DoesNotExist:
            raise serializers.ValidationError({"quote_id": "Quote not found."})

        # Validate availability date (not past)
        availability_date = attrs.get("availability_date")
        if availability_date and availability_date < timezone.now().date():
            raise serializers.ValidationError(
                {"availability_date": "Availability date cannot be in the past."}
            )

        # Validate proposed value
        if attrs.get("proposed_value") is not None:
            if attrs["proposed_value"] <= 0:
                raise serializers.ValidationError(
                    {"proposed_value": "Proposed value must be greater than 0."}
                )

        return attrs

    def create(self, validated_data):
        quote_id = validated_data.pop("quote_id")
        trader_id = validated_data.pop("trader_id")

        quote = QuoteRequest.objects.get(id=quote_id)
        trader = User.objects.get(id=trader_id)

        return QuoteBid.objects.create(quote=quote, trader=trader, **validated_data)


class QuoteBidUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteBid
        fields = ["proposed_value", "availability_date", "note"]

    def validate_availability_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Availability date cannot be in the past.")
        return value
