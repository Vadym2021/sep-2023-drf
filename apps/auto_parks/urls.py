from django.urls import path

from apps.auto_parks.views import AutoParkAddCarView, AutoParkListCreateView, AutoParkRetriveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
    path('/<int:pk>', AutoParkRetriveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy')
]
