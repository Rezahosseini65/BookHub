from rest_framework import serializers

from bookhub.apps.authors.models import Author


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'slug', 'image', 'url')


class AuthorDetailSerializer(serializers.ModelSerializer):
    book_author = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('id', 'name', 'slug', 'image', 'location', 'birthday', 'biography', 'book_author')

    def get_book_author(self, obj):
        from bookhub.apps.books.serializers import BookListSerializer
        books = obj.book_author.all()
        return BookListSerializer(books, many=True, read_only=True).data
