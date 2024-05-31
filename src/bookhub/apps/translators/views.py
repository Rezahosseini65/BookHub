from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from bookhub.apps.translators.models import Translator
from bookhub.apps.translators.serializers import TranslatorListSerializer, TranslatorDetailSerializer


# Create your views here.


class TranslatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Translator.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return TranslatorListSerializer
            case 'retrieve':
                return TranslatorDetailSerializer

            case _:
                raise NotAcceptable()

