from django.contrib import admin

from bookhub.apps.authors.models import Author


# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'location', 'birthday')
    prepopulated_fields = {'slug': ('name',)}
