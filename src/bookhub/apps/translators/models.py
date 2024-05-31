from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Translator(models.Model):
    name = models.CharField(_('name'), max_length=255, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, allow_unicode=True)
    image = models.ImageField(_('image'), null=True, blank=True, upload_to='images/translator/images/')
    birthday = models.DateField(_('birthday'), null=True, blank=True)
    biography = models.TextField(_('biography'), blank=True, null=True)

    class Meta:
        verbose_name = _('translator')
        verbose_name_plural = _('translators')

    def __str__(self):
        return self.name
