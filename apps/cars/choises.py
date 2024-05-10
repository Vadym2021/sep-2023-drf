from django.db.models import TextChoices


class CarChoises(TextChoices):
    Hatchback = 'Hatchback'
    Sedan = 'Sedan'
    Coupe = 'Coupe'
    Jeep = 'Jeep'
    Wagon = 'Wagon'
