from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import QuoteRequest
from .serializers import QuoteRequestSerializer,QuoteBidUpdateSerializer,QuoteBidSerializer
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



class CreateQuoteBidView(generics.CreateAPIView):
    serializer_class = QuoteBidSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["trader_id"] = request.user.id  # Force logged in user
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        bid = serializer.save()

        return Response(
            {"message": "Bid submitted successfully", "bid": serializer.data},
            status=status.HTTP_201_CREATED,
        )

class QuoteBidListForQuoteView(generics.ListAPIView):
    serializer_class = QuoteBidSerializer

    def get_queryset(self):
        quote_id = self.kwargs["quote_id"]
        return QuoteBid.objects.filter(quote_id=quote_id)


class UpdateQuoteBidView(generics.UpdateAPIView):
    queryset = QuoteBid.objects.all()
    serializer_class = QuoteBidUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        bid = self.get_object()

        # Ensuring only the worker who created it can update
        if bid.trader != request.user:
            return Response(
                {"error": "You are not allowed to submit this bid."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().update(request, *args, **kwargs)

