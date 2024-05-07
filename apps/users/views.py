from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializer import AutoParkSerializer
from apps.users.models import UserModel
from apps.users.serializer import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserAddAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        user = self.get_object()
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(auto_park_id=auto_park.id)
        serializer.save(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status.HTTP_201_CREATED)
