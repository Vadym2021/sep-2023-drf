from django.db import models


class CarManager(models.Manager):
    def get_audi_only(self):
        return self.filter(brand='audi')
