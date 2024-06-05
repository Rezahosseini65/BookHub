from rest_framework import serializers

from bookhub.apps.publishers.models import Publisher


class PublisherListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'slug', 'logo', 'url')


class PublisherDetailSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail',
        source='book_publisher'
    )

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'logo', 'founding_year', 'address', 'phone_number', 'description', 'books')

