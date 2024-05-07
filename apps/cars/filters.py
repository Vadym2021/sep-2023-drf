from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    sort_by = query.get('sort_by')
    if sort_by:
        if sort_by.startswith('-'):
            sort_field = sort_by[1:]
            qs = qs.order_by(f'-{sort_field}')
        else:
            qs = qs.order_by(sort_by)
        return qs

    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'year__gte':
                qs = qs.filter(year__gte=v)
            case 'year__lte':
                qs = qs.filter(year__lte=v)
            case 'brand_starts_with':
                qs = qs.filter(brand__startswith=v)
            case 'brand_ends_with':
                qs = qs.filter(brand__endswith=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)
            case _:
                raise ValidationError(f"{k} is not a valid filter")

    return qs

