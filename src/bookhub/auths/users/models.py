from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='profiles', verbose_name=_('user'))
    province = models.CharField(_('province'), max_length=64,
                                null=True, blank=True)
    city = models.CharField(_('city'), max_length=64, null=True, blank=True)
    address = models.CharField(_('address'), max_length=1024, null=True, blank=True)
    postal_code = models.CharField(_('postal code'), max_length=10,
                                   null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        