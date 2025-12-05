# models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_settings")

    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=True)
    calendar_reminders = models.BooleanField(default=True)
    marketing_emails = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def enable_all(self):
        self.email_notifications = True
        self.sms_notifications = True
        self.calendar_reminders = True
        self.marketing_emails = True
        self.save()

    def disable_all(self):
        self.email_notifications = False
        self.sms_notifications = False
        self.calendar_reminders = False
        self.marketing_emails = False
        self.save()

    def __str__(self):
        return f"Notification Settings for {self.user.email}"
