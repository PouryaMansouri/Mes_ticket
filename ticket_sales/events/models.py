from django.core.validators import RegexValidator
from django.db import models

from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

from customers.models import Customer


class Event(BaseModel):
    class Meta:
        verbose_name = _('رویداد')
        verbose_name_plural = _('رویداد')

    name = models.CharField(
        max_length=250,
        verbose_name=_('نام'),
    )

    total_capacity = models.PositiveIntegerField(
        verbose_name=_('ظرفیت کل')
    )

    remaining_capacity = models.PositiveIntegerField(
        verbose_name=_('ظرفیت باقیمانده'),
        editable=False,
    )

    price = models.PositiveIntegerField(
        verbose_name=_('قیمت'),
        help_text=_('قیمت به تومان'),
        default=0,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.remaining_capacity = self.total_capacity
        super().save(force_insert, force_update, using, update_fields)


class Ticket(BaseModel):
    class Meta:
        verbose_name = _('بلیت'),
        verbose_name_plural = _('بلیت')
        unique_together = ('event', 'national_code')

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_('مشتری'),
    )

    full_name = models.CharField(
        _('نام و نام خانوادگی'),
        max_length=150,
        blank=True
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name=_('رویداد'),
    )

    phone = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        verbose_name=_('شماره موبایل'),
        validators=[RegexValidator(
            regex='^(0)?9\d{9}$',
            message=_('Please Enter a Valid Phone Number!')
        )]
    )

    national_code = models.CharField(
        max_length=10,
        verbose_name=_('کدملی'),
        unique=True,
        validators=[RegexValidator(
            regex="^(?!(\d)\1{9})\d{10}$",
            message=_('National code isn\'t valid!')
        )]
    )
