from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import QuoteRequest
from .serializers import QuoteRequestSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Admin-only: Create job/quote
class QuoteRequestCreateView(generics.CreateAPIView):
    serializer_class = QuoteRequestSerializer
    permission_classes = [IsAdminUser]  # Only admins can create

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quote = serializer.save()
        return Response({
            "message": "Quote request created successfully",
            "quote": serializer.data
        }, status=status.HTTP_201_CREATED)


# Anyone can view/list jobs
class QuoteRequestListView(generics.ListAPIView):
    serializer_class = QuoteRequestSerializer
    permission_classes = [IsAuthenticated]  
    queryset = QuoteRequest.objects.all()
