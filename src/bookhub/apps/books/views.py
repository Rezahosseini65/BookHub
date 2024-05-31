from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from django_filters import rest_framework as filters

from bookhub.apps.books.filters import BookFilter
from bookhub.apps.books.models import Category, Book
from bookhub.apps.books.serializers import CategoryListSerializer, CategoryDetailSerializer, BookListSerializer, \
    BookDetailSerializer


# Create your views here.


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.is_public()

    def get_queryset(self):
        if self.action == 'list':
            return Category.get_root_nodes()
        return Category.objects.is_public()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryListSerializer
            case "retrieve":
                return CategoryDetailSerializer

            case _:
                raise NotAcceptable()


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.is_public()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter

    def get_serializer_class(self):
        match self.action:
            case "list":
                return BookListSerializer
            case "retrieve":
                return BookDetailSerializer

            case _:
                raise NotAcceptable()
