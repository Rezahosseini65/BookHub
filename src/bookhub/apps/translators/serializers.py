from rest_framework import serializers

from bookhub.apps.translators.models import Translator


class TranslatorListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translator
        fields = ('id', 'name', 'slug', 'image', 'url')


class TranslatorDetailSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='book-detail',
        source='book_translator'
    )

    class Meta:
        model = Translator
        fields = ('id', 'name', 'slug', 'image', 'birthday', 'biography', 'books')
