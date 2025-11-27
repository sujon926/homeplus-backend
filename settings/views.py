from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import AdminProfile
from .serializers import AdminProfileSerializer

class AdminProfileView(RetrieveUpdateAPIView):
    serializer_class = AdminProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return logged-in user's admin profile
        return self.request.user.admin_profile
