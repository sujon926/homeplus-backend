from rest_framework import serializers
from .models import TaskTemplate, Event

class TaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTemplate
        fields = ['id', 'title', 'default_cost']

class EventSerializer(serializers.ModelSerializer):
    # Read-only user to automatically assign logged-in user
    user = serializers.StringRelatedField(read_only=True)
    template = TaskTemplateSerializer(read_only=True)

    template_id = serializers.PrimaryKeyRelatedField(
        queryset=TaskTemplate.objects.all(), write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Event
        fields = [
            'id', 'user', 'template', 'template_id', 'title', 'date',
            'event_type', 'priority', 'estimated_cost', 'recurring',
            'compliance_type', 'requires_trade', 'description', 'created_at'
        ]
        read_only_fields = ['created_at', 'user']

    def create(self, validated_data):
        template = validated_data.pop('template_id', None)
        if template:
            validated_data['template'] = template
            if not validated_data.get('title'):
                validated_data['title'] = template.title
            if not validated_data.get('estimated_cost'):
                validated_data['estimated_cost'] = template.default_cost
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
