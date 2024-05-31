from django.contrib import admin

from bookhub.apps.translators.models import Translator

# Register your models here.


@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}