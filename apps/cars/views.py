from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import CarFilter
# from apps.cars.filters import car_filter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    # queryset = CarModel.objects.get_audi_only() #вызывает кастомный фильтр из managers.py
    serializer_class = CarSerializer
    filterset_class = CarFilter


    # def get_queryset(self):
    #     return car_filter(self.request.query_params)



class CarRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
