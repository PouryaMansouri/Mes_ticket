from django.core.validators import RegexValidator
from django.db import models

from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

from django_jalali.db import models as jmodels


class Event(BaseModel):
    class Meta:
        verbose_name = _('رویداد')
        verbose_name_plural = _('رویداد')

    title = models.CharField(
        max_length=250,
        verbose_name=_('عنوان'),
    )

    datetime = jmodels.jDateTimeField(
        verbose_name=_('زمان برگزاری'),
        null=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('توضیحات رویداد'),
    )

    image = models.ImageField(
        null=True,
        blank=True,
        default='events/default.jpg',
        upload_to='events',
        verbose_name=_('تصویر رویداد'),
        help_text=_('لطفا تصویری با عرض y و ارتفاع x پیکسل بارگذاری نمایید.')
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

    is_available = models.BooleanField(
        default=True,
        verbose_name=_('قابل استفاده بودن'),
        help_text=_('زمانی که ظرفیت رویداد به پایان برسد یا ادمین سایت این گزینه را لغو کند، امکان خرید بلیط برای این رویداد غیرفعال خواهد شد.')
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.pk:
            self.remaining_capacity = self.total_capacity
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title


class Ticket(BaseModel):
    class Meta:
        verbose_name = _('بلیط'),
        verbose_name_plural = _('بلیط')
        unique_together = ('event', 'national_code')

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

    is_used = models.BooleanField(
        default=False,
        verbose_name=_('استفاده شده'),
        help_text=_('زمانی که بلیط تحویل ورزشگاه شد، این فیلد باید توسط ادمین تغییر کند.')
    )


class Team(BaseModel):
    class Meta:
        verbose_name = _('تیم')
        verbose_name_plural = _('تیم')

    name = models.CharField(
        max_length=150,
        verbose_name=_('نام تیم')
    )

    logo = models.ImageField(
        null=True,
        blank=True,
        # default='events/default.jpg',
        upload_to='events/teams',
        verbose_name=_('لوگو'),
        help_text=_('لطفا تصویری با عرض y و ارتفاع x پیکسل بارگذاری نمایید.')
    )

