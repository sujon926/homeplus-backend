from django.urls import path, include
from .views import (
    SignupView, 
    LoginView, 
)

urlpatterns = [
    # Your custom authentication views
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'), 
]