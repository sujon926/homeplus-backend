from django.urls import path
from .views import QuoteRequestCreateView, QuoteRequestListView, QuoteBidCreateView,QuoteBidApproveRejectView,WorkerBidListView



urlpatterns = [
    path('post-job/', QuoteRequestCreateView.as_view(), name='create-quote'),
    path('job-list/', QuoteRequestListView.as_view(), name='list-quote'),
    path('quotes/<int:quote_id>/bid/', QuoteBidCreateView.as_view(), name='bid-quote'),
    path('bid/<int:id>/status/', QuoteBidApproveRejectView.as_view(), name='approve-reject-bid'),
    path('worker/bids/', WorkerBidListView.as_view(), name='worker-bids'),
]
