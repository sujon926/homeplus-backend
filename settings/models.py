from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class AdminProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="admin_profile"
    )
   
    profile_image = CloudinaryField("admin_profile", blank=True, null=True)  
    phone = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return self.user.email



