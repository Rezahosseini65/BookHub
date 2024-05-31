from rest_framework import serializers

from bookhub.apps.publishers.models import Publisher


class PublisherListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'slug', 'logo')


class PublisherDetailSerializer(serializers.ModelSerializer):
    book_publisher = serializers.SerializerMethodField()

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'logo', 'founding_year', 'address', 'phone_number', 'description', 'book_publisher')

    def get_book_publisher(self, obj):
        from bookhub.apps.books.serializers import BookListSerializer
        books = obj.book_publisher.all()
        return BookListSerializer(books, many=True, read_only=True).data