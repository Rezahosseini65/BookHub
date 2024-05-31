from rest_framework import serializers

from bookhub.apps.authors.serializers import AuthorListSerializer
from bookhub.apps.books.models import Category, Book, BookImage
from bookhub.apps.inventory.models import StockRecord
from bookhub.apps.publishers.serializers import PublisherListSerializers
from bookhub.apps.translators.serializers import TranslatorListSerializer


class CategoryListSerializer(serializers.ModelSerializer):
    breadcrumbs = serializers.CharField(source='full_name', read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'breadcrumbs')


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'children')

    def get_children(self, obj):
        children = obj.get_children()
        return CategoryListSerializer(children, many=True).data


class BookImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BookImage
        fields = ('book', 'image', 'display_order', 'image_url')

    def get_image_url(self, obj):
        image_instance = obj.image
        if image_instance:
            return image_instance.image.url
        return None


class BookListSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'slug', 'page_count', 'publication_year',
                  'edition', 'images')


class StockRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecord
        fields = ('sale_price', )


class BookDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    translator = TranslatorListSerializer(many=True, read_only=True)
    author = AuthorListSerializer(many=True, read_only=True)
    images = BookImageSerializer(many=True, read_only=True)
    publisher = PublisherListSerializers(many=True, read_only=True)
    stockrecords = StockRecordSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'slug','meta_title', 'description',
                  'meta_description', 'page_count', 'publication_year', 'edition',
                  'is_discountable', 'category', 'translator', 'publisher',
                  'author', 'images', 'stockrecords')
