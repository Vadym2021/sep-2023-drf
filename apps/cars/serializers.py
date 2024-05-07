from rest_framework import serializers
from .models import CarModel


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     brand = serializers.CharField(max_length=50)
#     year = serializers.IntegerField()
#     seats = serializers.IntegerField()
#     engine = serializers.FloatField()
#
#     def create(self, validated_data):
#         car = CarModel.objects.create(**validated_data)
#         return car
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'year')
