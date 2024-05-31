from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class StockRecord(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE,
                             related_name='stockrecords', verbose_name=_('stock record'))
    sku = models.CharField(_('SKU'), max_length=64, blank=True, null=True, unique=True)
    buy_price = models.PositiveIntegerField(_('buy price'), blank=True, null=True)
    sale_price = models.PositiveIntegerField(_('sale price'), blank=True, null=True)
    num_stock = models.PositiveIntegerField(_('num stock'), default=0)
