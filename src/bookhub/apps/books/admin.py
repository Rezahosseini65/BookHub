from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from bookhub.apps.books.models import Category, BookImage, Book, BookRecommendation
from bookhub.apps.inventory.models import StockRecord


# Register your models here.

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    prepopulated_fields = {'slug': ('name',)}


class BookImageInLine(admin.StackedInline):
    model = BookImage
    extra = 2


class StockRecordInLine(admin.StackedInline):
    model = StockRecord
    extra = 1


class BookRecommendationInline(admin.StackedInline):
    model = BookRecommendation
    extra = 2
    fk_name = 'primary'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public', 'publication_year', 'edition',
                    'created', 'updated', 'is_discountable', 'track_stock',
                    'require_shipping', 'page_count')
    list_filter = ('is_public', 'page_count', 'is_discountable', 'track_stock', 'require_shipping')
    list_editable = ('is_public', 'is_discountable', 'track_stock', 'require_shipping')
    search_fields = ('name', 'description')
    filter_horizontal = ('publisher', 'author', 'translator')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [BookImageInLine, StockRecordInLine, BookRecommendationInline]


admin.site.register(Category, CategoryAdmin)
