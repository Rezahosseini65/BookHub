from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from bookhub.apps.publishers.models import Publisher
from bookhub.apps.publishers.serializers import PublisherListSerializers, PublisherDetailSerializer


# Create your views here.


class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()

    def get_serializer_class(self):
        match self.action:
            case "list":
                return PublisherListSerializers
            case "retrieve":
                return PublisherDetailSerializer

            case _:
                raise NotAcceptable()