from rest_framework import serializers
from .models import AdminProfile
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _

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
            instance.user.name = name
            instance.user.save()

        # Update phone
        instance.phone = validated_data.get("phone", instance.phone)
        instance.save()

        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["name"] = instance.user.name or ""
        return data



# password chnage
class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        write_only=True, required=True,
        style={'input_type': 'password'},
        error_messages={'required': _('Current password is required')}
    )
    new_password = serializers.CharField(
        write_only=True, required=True,
        validators=[validate_password],
        style={'input_type': 'password'},
        error_messages={'required': _('New password is required')}
    )
    confirm_new_password = serializers.CharField(
        write_only=True, required=True,
        style={'input_type': 'password'},
        error_messages={'required': _('Please confirm your new password')}
    )

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(_('Current password is incorrect'))
        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({'confirm_new_password': _('New passwords do not match')})
        if attrs['current_password'] == attrs['new_password']:
            raise serializers.ValidationError({'new_password': _('New password cannot be the same as the current password')})
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user