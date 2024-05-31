from django_filters import rest_framework as filters

from bookhub.apps.books.models import Book


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publisher = filters.CharFilter(field_name='publisher__name', lookup_expr='icontains')
    translator = filters.CharFilter(field_name='translator__name', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='stockrecords__sale_price', lookup_expr='lte')
    max_price = filters.NumberFilter(field_name='stockrecords__sale_price', lookup_expr='gte')
    created__gte = filters.DateFilter(field_name='created', lookup_expr='gte')
    created__lte = filters.DateFilter(field_name='created', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'translator', 'min_price', 'max_price')