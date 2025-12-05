from rest_framework import serializers
from .models import NotificationPreference

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreference
        fields = (
            "email_notifications",
            "sms_notifications",
            "calendar_reminders",
            "marketing_emails",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")
