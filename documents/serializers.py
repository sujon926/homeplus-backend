from rest_framework import serializers
from .models import UserDocument
from datetime import date


class UserDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocument
        fields = ["id", "document_type", "file", "validity_date"]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        """Return Cloudinary URL instead of the whole object."""
        data = super().to_representation(instance)
        data["file"] = instance.file.url if instance.file else None
        return data

    def validate(self, data):
        """Ensure validity date is not in the past."""
        validity = data.get("validity_date")  # safe for partial update
        if validity and validity < date.today():
            raise serializers.ValidationError("Validity date cannot be in the past.")
        return data
