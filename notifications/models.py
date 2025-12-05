from django.conf import settings
from django.db import models
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class NotificationSettings(models.Model):
    """
    Stores per-user notification preferences (one-to-one with User).
    Each field corresponds to a toggle in the UI (on/off).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_settings")
    email_notifications = models.BooleanField(
        default=True,
        help_text="Receive updates via email"
    )
    sms_notifications = models.BooleanField(
        default=False,
        help_text="Receive urgent alerts via SMS"
    )
    calendar_reminders = models.BooleanField(
        default=False,
        help_text="Add events to your calendar"
    )
    marketing_emails = models.BooleanField(
        default=False,
        help_text="Receive tips and offers"
    )

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notification Settings"
        verbose_name_plural = "Notification Settings"

    def __str__(self):
        return f"NotificationSettings(user={self.user})"

    # Convenience methods
    def to_dict(self):
        return {
            "email_notifications": self.email_notifications,
            "sms_notifications": self.sms_notifications,
            "calendar_reminders": self.calendar_reminders,
            "marketing_emails": self.marketing_emails,
        }

    def enable_all(self):
        self.email_notifications = True
        self.sms_notifications = True
        self.calendar_reminders = True
        self.marketing_emails = True
        self.save(update_fields=[
            "email_notifications", "sms_notifications", "calendar_reminders", "marketing_emails", "updated_at"
        ])

    def disable_all(self):
        self.email_notifications = False
        self.sms_notifications = False
        self.calendar_reminders = False
        self.marketing_emails = False
        self.save(update_fields=[
            "email_notifications", "sms_notifications", "calendar_reminders", "marketing_emails", "updated_at"
        ])
