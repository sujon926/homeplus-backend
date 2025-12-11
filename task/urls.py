from django.urls import path
from .views import (
    TaskTemplateListCreateView, TaskTemplateRetrieveUpdateDestroyView,
    EventListCreateView, EventRetrieveUpdateDestroyView
)

urlpatterns = [
    # TaskTemplate URLs
    path('task-templates/', TaskTemplateListCreateView.as_view(), name='tasktemplate-list-create'),
    path('task-templates/<int:pk>/', TaskTemplateRetrieveUpdateDestroyView.as_view(), name='tasktemplate-detail'),

    # Event URLs
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
]
