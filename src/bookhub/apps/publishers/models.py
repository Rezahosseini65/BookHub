from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(_('name'), max_length=255, db_index=True)
    slug = models.SlugField(_('slug'), max_length=255, allow_unicode=True, unique=True)
    logo = models.ImageField(_('logo'), null=True, blank=True)
    founding_year = models.CharField(_('founding year'), max_length=4)
    address = models.TextField(_('address'), blank=True, null=True)
    phone_number = models.CharField(_('phone number'), max_length=12,
                                    null=True, blank=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('Publishers')

    def __str__(self):
        return self.name
