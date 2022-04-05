from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models

from core.models import SingletonBaseModel
from django.utils.translation import gettext_lazy as _


class SiteSetting(SingletonBaseModel):
    class Meta:
        verbose_name = _('تنظیمات سایت')
        verbose_name_plural = _('تنظیمات سایت')

    site_name = models.CharField(
        max_length=100,
        verbose_name=_('نام سایت'),
    )

    bg_image = models.ImageField(
        null=True,
        blank=True,
        default='site_settings/bg.jpg',
        upload_to='site_settings',
        verbose_name=_('تصویر پس زمینه'),
        help_text=_('لطفا تصویری با عرض ۸۳۰ و ارتفاع ۴۸۰ پیکسل بارگذاری نمایید.')
    )

    home_banner = models.ImageField(
        null=True,
        blank=True,
        default='site_settings/banner.png',
        upload_to='site_settings',
        verbose_name=_('بنر صفحه اصلی'),
        help_text=_('لطفا تصویری با عرض ۷۴۰ و ارتفاع ۱۱۰ پیکسل بارگذاری نمایید.')
    )

    contact_phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_('تلفن ارتباطی'),
        help_text=_('این شماره تلفن ثابت شماست. لطفا آن را با پیش شماره شهر خود وارد نمایید.'),
        validators=[RegexValidator(
            regex='^0\d{2,3}\d{8}$',
            message=_('لطفا شماره تلفن معتبری وارد نمایید.')
        )]
    )

    contact_email = models.EmailField(
        verbose_name=_('آدرس ایمیل ارتباطی'),
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('توضیحات سایت'),
        help_text=_('این توضیحات در بخش پاورقی وبسایت نمایش داده خواهند شد.'),
    )

    site_name_color = ColorField(
        default='#FFFFFF',
        verbose_name=_('رنگ تیتر سایت'),
        blank=True,
    )

    navbar_text_color = ColorField(
        default='#FFFFFF',
        verbose_name=_('رنگ متن نوار بالای سایت'),
        blank=True,
    )

    footer_text_color = ColorField(
        default='#FFFFFF',
        verbose_name=_('رنگ متن پاورقی سایت'),
        blank=True,
    )

    def __str__(self):
        return self.site_name
