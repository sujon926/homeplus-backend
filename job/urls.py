from django.urls import path
from .views import QuoteRequestCreateView,QuoteRequestListView

urlpatterns = [
    path('post-job/', QuoteRequestCreateView.as_view(), name='create-quote'),
    path('job-list/', QuoteRequestListView.as_view(), name='lis-quote'),
]
