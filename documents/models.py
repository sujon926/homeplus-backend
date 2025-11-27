import os
from django.db import models
from django.core.exceptions import ValidationError
from .enums import DocumentType
from common.models import TimeStampedModel
from cloudinary.models import CloudinaryField


def validate_file_size(file):
    max_size_mb = 10
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size exceeds {max_size_mb}MB limit.")


def validate_file_extension(file):
    allowed_extensions = ["pdf", "png", "jpg", "jpeg", "doc", "docx"]
    ext = file.name.split('.')[-1].lower()
    if ext not in allowed_extensions:
        raise ValidationError("Unsupported file type.")


class UserDocument(TimeStampedModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    document_type = models.CharField(
        max_length=20,
        choices=DocumentType.choices
    )

    file = CloudinaryField(
        resource_type="raw",
        folder="documents/",
        validators=[validate_file_size, validate_file_extension]
    )

    validity_date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.document_type}"

