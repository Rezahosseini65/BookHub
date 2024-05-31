from rest_framework import serializers

from bookhub.apps.translators.models import Translator


class TranslatorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translator
        fields = ('id', 'name', 'slug', 'image')


class TranslatorDetailSerializer(serializers.ModelSerializer):
    book_translator = serializers.SerializerMethodField()

    class Meta:
        model = Translator
        fields = ('id', 'name', 'slug', 'image', 'birthday', 'biography', 'book_translator')

    def get_book_translator(self, obj):
        from bookhub.apps.books.serializers import BookListSerializer
        books = obj.book_translator.all()
        return BookListSerializer(books, many=True, read_only=True).data
