from rest_framework import serializers
from .models import AdminProfile

class AdminProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = AdminProfile
        fields = ["name", "email", "phone"]

    def update(self, instance, validated_data):
        # Update Name (writes to user model)
        name = validated_data.pop("name", None)
        if name:
            parts = name.strip().split(" ", 1)
            instance.user.first_name = parts[0]
            instance.user.last_name = parts[1] if len(parts) > 1 else ""
            instance.user.save()

        # Update phone
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()

        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        first = instance.user.first_name or ""
        last = instance.user.last_name or ""
        data["name"] = f"{first} {last}".strip()
        return data
