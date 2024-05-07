from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import UserModel
from .serializer import UserSerializer


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
