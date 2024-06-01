from django.db.models import Prefetch

from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from django_filters import rest_framework as filters

from bookhub.apps.authors.models import Author
from bookhub.apps.books.filters import BookFilter
from bookhub.apps.books.models import Category, Book
from bookhub.apps.books.serializers import CategoryListSerializer, CategoryDetailSerializer, BookListSerializer, \
    BookDetailSerializer
from bookhub.apps.publishers.models import Publisher
from bookhub.apps.translators.models import Translator


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

    def get_queryset(self):
        """
        Retrieve the queryset of books with related authors, publishers, translators, and category.

        Returns:
                QuerySet: A queryset of Book objects with select_related and prefetch_related applied on related models.
        """
        author_prefetch = Prefetch('author',
                                   queryset=Author.objects.all())
        publisher_prefetch = Prefetch('publisher',
                                      queryset=Publisher.objects.all())
        translator_prefetch = Prefetch('translator',
                                       queryset=Translator.objects.all())
        return Book.objects.is_public().select_related('category').prefetch_related(
            author_prefetch,
            publisher_prefetch,
            translator_prefetch
        )