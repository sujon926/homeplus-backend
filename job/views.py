from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import QuoteRequest
from .serializers import QuoteRequestSerializer,QuoteBidSerializer,QuoteBidStatusUpdateSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import QuoteBid




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

# create bid



# Worker/Trader: Bid on a job
class QuoteBidCreateView(generics.CreateAPIView):
    serializer_class = QuoteBidSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, quote_id, *args, **kwargs):
        try:
            quote = QuoteRequest.objects.get(id=quote_id)
        except QuoteRequest.DoesNotExist:
            return Response({"detail": "Quote not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(worker=request.user, quote=quote)
        return Response({"message": "Bid submitted successfully", "bid": serializer.data}, status=status.HTTP_201_CREATED)



class QuoteBidApproveRejectView(generics.UpdateAPIView):
    queryset = QuoteBid.objects.all()
    serializer_class = QuoteBidStatusUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class WorkerBidListView(generics.ListAPIView):
    serializer_class = QuoteBidSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return QuoteBid.objects.filter(worker=self.request.user)

