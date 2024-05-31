from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Author(models.Model):
    name = models.CharField(_('name'), max_length=255, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    image = models.ImageField(_('image'), blank=True, null=True,
                              upload_to='images/authors/images/')
    location = models.CharField(_('location'), max_length=255, null=True, blank=True)
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    biography = models.TextField(_('biography'), blank=True, null=True)

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.name
