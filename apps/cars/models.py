from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParkModel
from apps.cars.choises import CarChoises
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = "cars"
        ordering = ('id',)

    # brand = models.CharField(max_length=50, validators=[V.MinLengthValidator(3)])
    brand = models.CharField(max_length=50, validators=[V.RegexValidator('^[A-Z][a-zA-z]{2,49}$',[
        'first letter uppercase',
        'min 3',
        'max 50'
    ])])
    price = models.IntegerField(validators=[V.MinValueValidator(9),V.MaxValueValidator(1000000)])
    year = models.IntegerField(validators=[V.MinValueValidator(1990),V.MaxValueValidator(datetime.now().year)])
    chassis = models.CharField(max_length=50, choices=[*CarChoises.choices])
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='users')

