from django.db import models

class CarModel(models.Model):
    class Meta:
        db_table = "cars"
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    seats = models.IntegerField()
    chasis = models.CharField(max_length=50)
    engine = models.FloatField()
