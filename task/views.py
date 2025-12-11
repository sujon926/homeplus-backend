from rest_framework import generics, permissions, filters
from .models import TaskTemplate, Event
from .serializers import TaskTemplateSerializer, EventSerializer

# ---------------- TaskTemplate ----------------
class TaskTemplateListCreateView(generics.ListCreateAPIView):
    queryset = TaskTemplate.objects.all()
    serializer_class = TaskTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'default_cost']

class TaskTemplateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskTemplate.objects.all()
    serializer_class = TaskTemplateSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can update/delete

# ---------------- Event ----------------
class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['date', 'priority']

    def get_queryset(self):
        # Users see only their own events
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Event deleted successfully."}, 
            status=status.HTTP_200_OK
        )

