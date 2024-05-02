from django.urls import path
# from cars.views import CarTestView, CarDetailsView
from apps.cars.views import CarListCreateView, CarRetriveUpdateDestroyView

urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # path('carsDetail/<int:pk>', CarDetailsView.as_view()),
    # path('carsDetail/<str:pk>', CarDetailsView.as_view()),
    # path('carsDetail/<str:pk>', CarDetailsView.as_view()), # строка без спецсимволов, проходят буквы цифры и _
    path('', CarListCreateView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarRetriveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy')
]
