from django.db import models
from django.conf import settings

class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="emailsecurity_profile"
    )
    phone = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return self.user.email
