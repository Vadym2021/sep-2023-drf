from rest_framework import serializers

from apps.auto_parks.serializer import AutoParkSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'auto_parks')
        depth = 1
