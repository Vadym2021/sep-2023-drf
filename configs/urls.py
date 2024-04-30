from django.urls import path
# from cars.views import CarTestView, CarDetailsView
from  cars.views import CarListCreateView, CarRetriveUpdateDestroyView

urlpatterns = [
    # path('carsTest', CarTestView.as_view()),
    # path('carsDetail/<int:pk>', CarDetailsView.as_view()),
    # path('carsDetail/<str:pk>', CarDetailsView.as_view()),
    # path('carsDetail/<str:pk>', CarDetailsView.as_view()), # строка без спецсимволов, проходят буквы цифры и _
    path('cars', CarListCreateView.as_view()),
    path('cars/<int:pk>',CarRetriveUpdateDestroyView.as_view())
]
