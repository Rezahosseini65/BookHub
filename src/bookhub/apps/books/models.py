import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from treebeard.mp_tree import MP_Node

from bookhub.apps.books.managers import CategoryQuerySet, BookQuerySet

# Create your models here.

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Category(MP_Node):
    name = models.CharField(_('name'), max_length=255, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    is_public = models.BooleanField(_('is public'), default=True)
    description = models.TextField(_('description'), blank=True, null=True)

    objects = CategoryQuerySet.as_manager()

    _full_name_separator = " > "

    @property
    def full_name(self):
        """
        Property that returns the full name of a category by joining the names of all ancestors and itself.
        returns:
            str: The full name of the category.
        """
        names = [category.name for category in self.get_ancestors_and_self()]
        return self._full_name_separator.join(names)

    def get_ancestors_and_self(self):
        """
        Returns a list of ancestors and the category itself.

        If the category is the root, it returns a list containing only itself.

        returns:
            list: A list of ancestors and the category itself.
        """
        if self.is_root():
            return [self]
        return list(self.get_ancestors()) + [self]

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['path']
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='books', verbose_name=_('category'))
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    is_public = models.BooleanField(_('is public'), default=True)
    meta_title = models.CharField(_('meta title'), max_length=512,
                                  blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    meta_description = models.CharField(_('meta description'), max_length=1024,
                                        blank=True, null=True)
    page_count = models.PositiveIntegerField(_('page count'), default=0)
    publication_year = models.CharField(_('publication year'), max_length=4)
    edition = models.CharField(_('edition'), max_length=4, default='1')
    pdf = models.FileField(_('PDF'), blank=True, null=True, upload_to='files/pdf/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_discountable = models.BooleanField(_('Is Discountable?'), default=True)
    track_stock = models.BooleanField(_('Track Stock'), default=True)
    require_shipping = models.BooleanField(_('Require Shipping?'), default=True)

    translator = models.ManyToManyField('translators.Translator', related_name='book_translator',
                                        verbose_name=_('translator'))
    publisher = models.ManyToManyField('publishers.Publisher', related_name='book_publisher',
                                       verbose_name=_('publisher'))
    author = models.ManyToManyField('authors.Author', related_name='book_author',
                                    verbose_name=_('author'))
    recommended_book = models.ManyToManyField('books.Book', through='BookRecommendation',
                                              blank=True, verbose_name=_('Recommended book'))

    objects = BookQuerySet.as_manager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['created']),
        ]
        verbose_name = _('book')
        verbose_name_plural = (_('books'))

    def __str__(self):
        return f"{self.category.full_name}--{self.name}"


class BookRecommendation(models.Model):
    primary = models.ForeignKey(Book, on_delete=models.CASCADE,
                                related_name='primary_recommendation', verbose_name=_('Primary book'))
    recommendation = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('Recommendation book'))
    rank = models.PositiveSmallIntegerField(_('Rank'), default=0, db_index=True)

    class Meta:
        ordering = ('primary', '-rank')
        unique_together = ('primary', 'recommendation')
        verbose_name = _('book recommendation')
        verbose_name_plural = _('book recommendations')


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ForeignKey('media.Image', on_delete=models.PROTECT)

    display_order = models.PositiveSmallIntegerField(_('Display order'), default=0)

    def delete(self, *args, **kwargs):
        """
        This method is called when an instance of the model is deleted.
        It ensures that the default behavior of the `delete` method is preserved.
        Additionally, it updates the `display_order` field for related images.
        """

        super().delete(*args, **kwargs)

        for index, image in enumerate(self.book.images.all()):
            image.display_order = index
            image.save()

    class Meta:
        ordering = ('display_order',)
        verbose_name = _('book image')
        verbose_name_plural = _('book images')
