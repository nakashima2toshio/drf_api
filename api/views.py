from django.shortcuts import render
from rest_framework import viewsets, permissions
from api.models import CustomUser, CustomUserProfile
from api.serializers import CustomUserSerializer, ProfileSerializer
from sns_app.models import Profile as SnsProfile

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return CustomUser.objects.filter(id=user.id)
        return CustomUser.objects.none()

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = SnsProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return SnsProfile.objects.filter(custom_user=user)
        return SnsProfile.objects.none()


# class ManageUserView(generics.RetrieveUpdateAPIView):
#     serializer_class = CustomUserSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return self.request.user

