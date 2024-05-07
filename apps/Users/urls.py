from django.urls import path

from apps.Users.views import UserListView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>/add_car', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
    path('/<int:pk>', AutoParkRetriveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy')
]