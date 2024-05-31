from django.contrib import admin

from bookhub.apps.publishers.models import Publisher


# Register your models here.


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'founding_year')
    prepopulated_fields = {'slug': ('name',)}
