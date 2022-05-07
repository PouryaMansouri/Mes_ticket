from django.db import models

from core.models import SingletonBaseModel
from django.utils.translation import gettext_lazy as _


class SiteSetting(SingletonBaseModel):
    class Meta:
        verbose_name = _('تنظیمات سایت')
        verbose_name_plural = _('تنظیمات سایت')

    home_banner = models.ImageField(
        null=True,
        blank=True,
        upload_to='site_settings',
        verbose_name=_('بنر صفحه اصلی'),
        help_text=_('لطفا تصویری با عرض ۱۹۲۰ و ارتفاع ۸۱۰ پیکسل بارگذاری نمایید.')
    )

    home_link = models.URLField(
        null=True,
        blank=True,
        default='belitmes.ir',
        verbose_name=_('لینک صفحه اصلی'),
    )

    kavenegar_api_key = models.CharField(
        max_length=150,
        verbose_name=_('کد API key کاوه نگار'),
        null=True,
        blank=True
    )

    kavenegar_sender = models.CharField(
        max_length=150,
        verbose_name=_('فرستنده پیامک کاوه نگار'),
        null=True,
        blank=True
    )

    def __str__(self):
        return 'تنظیمات سایت'
