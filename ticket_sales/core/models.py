from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from core.manager import MyUserManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('Create Timestamp'),
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('Update Timestamp'),
    )


class User(AbstractUser):
    objects = MyUserManager()

    phone = models.CharField(
        max_length=14,
        verbose_name=_('Phone'),
        unique=True,
        validators=[RegexValidator(
            regex='^(0)?9\d{9}$',
            message=_('Please Enter a Valid Phone Number!')
        )]
    )

    national_code = models.CharField(
        max_length=10,
        verbose_name=_('National Code'),
        unique=True,
        validators=[RegexValidator(
            regex="^(?!(\d)\1{9})\d{10}$",
            message=_('National code isn\'t valid!')
        )]
    )

    USERNAME_FIELD = 'phone'

    def save(self, *args, **kwargs):
        self.username = self.phone
        super().save(*args, **kwargs)


class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
