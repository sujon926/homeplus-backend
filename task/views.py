from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TaskTemplateSerializer,EventSerializer
from .models import TaskTemplate,Event
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers




# Create your views here.
class TaskTemplateListView(generics.ListAPIView):
    serializer_class = TaskTemplateSerializer
    queryset = TaskTemplate.objects.all()


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=400)
        except Exception as e:
            return Response(
                {"detail": "Something went wrong", "error": str(e)},
                status=500
            )


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
