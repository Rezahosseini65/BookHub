from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from bookhub.apps.authors.models import Author
from bookhub.apps.authors.serializers import AuthorListSerializer, AuthorDetailSerializer


# Create your views here.


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return AuthorListSerializer
            case 'retrieve':
                return AuthorDetailSerializer

            case _:
                raise NotAcceptable()
