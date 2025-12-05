from rest_framework import serializers 
from .models import TaskTemplate, Event



class TaskTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTemplate
        fields = ["id", "title", "default_cost"]
        

class EventSerializer(serializers.ModelSerializer):
    template = TaskTemplateSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id", "template", "title", "date",
            "event_type", "priority",
            "estimated_cost", "recurring",
            "compliance_type", "requires_trade",
            "description"
        ]

    def validate(self, data):
        if not data.get("title"):
            raise serializers.ValidationError({"title": "Event title is required."})

        if not data.get("event_type"):
            raise serializers.ValidationError({"event_type": "Event type is required."})

        if not data.get("priority"):
            raise serializers.ValidationError({"priority": "Priority is required."})

        if not data.get("date"):
            raise serializers.ValidationError({"date": "Event date is required."})

        return data

    def create(self, validated_data):
        user = self.context["request"].user
        return Event.objects.create(user=user, **validated_data)
