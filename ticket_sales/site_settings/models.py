from django.db import models

from core.models import SingletonBaseModel
from django.utils.translation import gettext_lazy as _


class SiteSetting(SingletonBaseModel):
    class Meta:
        verbose_name = _('تنظیمات سایت')
        verbose_name_plural = _('تنظیمات سایت')

    kavenegar_api_key = models.CharField(
        max_length=150,
        verbose_name=_('کد API key کاوه نگار')
    )

    kavenegar_sender = models.CharField(
        max_length=150,
        verbose_name=_('فرستنده پیامک کاوه نگار')
    )

    def __str__(self):
        return 'site setting'
