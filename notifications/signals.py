# signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NotificationSettings

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_notification_settings(sender, instance, created, **kwargs):
    if created:
        NotificationSettings.objects.create(user=instance)


from django.apps import AppConfig

class NotificationsAppConfig(AppConfig):
    name = "notifications"

    def ready(self):
        # import signals so they get registered
        import notifications.signals  # noqa
