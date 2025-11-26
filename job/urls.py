from django.urls import path
from .views import (
    QuoteRequestCreateView,
    QuoteRequestListView,
    CreateQuoteBidView,
    UpdateQuoteBidView,
    QuoteBidListForQuoteView,
    # AdminAllBidsListView

)

urlpatterns = [
    # Job (Quote Request)
    path('post-job/', QuoteRequestCreateView.as_view(), name='create-quote'),
    path('job-list/', QuoteRequestListView.as_view(), name='list-quote'),

    # Bids
    path('bids/create/', CreateQuoteBidView.as_view(), name='create-bid'),
    path('bids/<int:id>/update/', UpdateQuoteBidView.as_view(), name='update-bid'),
    path('quotes/<int:quote_id>/bids/', QuoteBidListForQuoteView.as_view(), name='quote-bids'),

    # Admin
    # path('admin/bids/', AdminAllBidsListView.as_view(), name='admin-all-bids'),
]
