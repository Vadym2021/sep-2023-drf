from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    brand = filters.CharFilter('brand', 'icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'price',
            ('year', 'asd')
            # Если надо переназвать год на асд, тогд можна сортировать по асд в квери, но фактически по году
        )
    )

# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import ValidationError
#
# from apps.cars.models import CarModel
#
#
# def car_filter(query: QueryDict) -> QuerySet:
#     qs = CarModel.objects.all()
#
#     filters = {}
#     sort_by = None
#
#     for k, v in query.items():
#         match k:
#             case 'price_gt':
#                 filters['price__gt'] = v
#             case 'price_lt':
#                 filters['price__lt'] = v
#             case 'year__gte':
#                 filters['year__gte'] = v
#             case 'year__lte':
#                 filters['year__lte'] = v
#             case 'brand_starts_with':
#                 filters['brand__startswith'] = v
#             case 'brand_ends_with':
#                 filters['brand__endswith'] = v
#             case 'brand_contains':
#                 filters['brand__icontains'] = v
#             case 'sort_by':
#                 sort_by = v
#             case 'page':
#                 # Do nothing, page will be handled separately
#                 pass
#             case 'size':
#                 # Ignore size parameter
#                 pass
#             case _:
#                 raise ValidationError(f"{k} is not a valid filter")
#
#     for field, value in filters.items():
#         qs = qs.filter(**{field: value})
#
#     if sort_by:
#         if sort_by.startswith('-'):
#             sort_field = sort_by[1:]
#             qs = qs.order_by(f'-{sort_field}')
#         else:
#             qs = qs.order_by(sort_by)
#
#     paginator = Paginator(qs, 10)  # Default page size is 10
#     page = query.get('page')
#     try:
#         qs = paginator.page(page)
#     except PageNotAnInteger:
#         qs = paginator.page(1)
#     except EmptyPage:
#         qs = paginator.page(paginator.num_pages)
#
#     return qs
#
#
#
