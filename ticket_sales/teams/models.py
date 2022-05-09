from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Team(BaseModel):
    class Meta:
        verbose_name = _('تیم')
        verbose_name_plural = _('تیم')

    name = models.CharField(
        max_length=50, verbose_name=_('نام تیم')
    )
    logo = models.ImageField(
        upload_to='teams/', verbose_name=_('لوگوی تیم'),
        blank=True, null=True,
        help_text = 'لطفا تصویری با طول x و عرض y بارگزاری کنید.'
    )

    def __str__(self):
        return self.name
