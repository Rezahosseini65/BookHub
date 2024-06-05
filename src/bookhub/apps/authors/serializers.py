from rest_framework import serializers

from bookhub.apps.authors.models import Author


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'slug', 'image', 'url')


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail',
        source='book_author'
    )

    class Meta:
        model = Author
        fields = ('id', 'name', 'slug', 'image', 'location', 'birthday', 'biography', 'books')

