from rest_framework import views
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import CustomUser
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .ownpermissions import ProfilePermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ProfilePermission,)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # authentication_classes = TokenAuthentication,
    # permission_classes = (IsAuthenticated,)


class SampleAPIView(views.APIView):

    def get(self, request, *args, **option):
        return


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user




