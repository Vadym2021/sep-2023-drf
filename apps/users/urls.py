from django.urls import path

from apps.users.views import UserAddAutoParkView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_view'),
    path('/<int:pk>/add_auto_park', UserAddAutoParkView.as_view(), name='users_add_auto_park'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy')
]