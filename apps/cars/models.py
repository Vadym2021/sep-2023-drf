from django.db import models
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = "cars"

    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    seats = models.IntegerField()
    chasis = models.CharField(max_length=50)
    engine = models.FloatField()
