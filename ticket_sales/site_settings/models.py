from django.core.validators import RegexValidator
from django.db import models

from core.models import SingletonBaseModel
from django.utils.translation import gettext_lazy as _


class SiteSetting(SingletonBaseModel):
    class Meta:
        verbose_name = _('Site Setting')
        verbose_name_plural = _('Site Settings')

    site_name = models.CharField(
        max_length=100,
        verbose_name=_('Site Name'),
    )

    home_banner = models.ImageField(
        null=True,
        blank=True,
        default='site_settings/default_customer.png',
        upload_to='site_settings',
        verbose_name=_('Home Banner'),
        help_text=_('Please upload an image with x width and y height!')
    )

    contact_phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_('Contact Phone'),
        help_text=_('This is const phone. write it with pre number!'),
        validators=[RegexValidator(
            regex='^0\d{2,3}\d{8}$',
            message=_('Please Enter a Valid Phone!')
        )]
    )

    email = models.EmailField(
        verbose_name=_('Email Address'),
    )

    def __str__(self):
        return self.site_name
