from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializer import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkListView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AutoParkRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(auto_park_id=auto_park.id)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParkSerializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)
