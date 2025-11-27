from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import AdminProfile
from .serializers import AdminProfileSerializer,ChangePasswordSerializer
from django.contrib.auth import update_session_auth_hash
from rest_framework import generics, permissions, status
from rest_framework.response import Response



class AdminProfileView(RetrieveUpdateAPIView):
    serializer_class = AdminProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return logged-in user's admin profile
        return self.request.user.admin_profile


# ---------------------- Change Password ---------------------- #
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        update_session_auth_hash(request, serializer.instance)
        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)