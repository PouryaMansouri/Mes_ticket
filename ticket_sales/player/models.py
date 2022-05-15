from django.db import models
from django.utils.translation import gettext_lazy as _


class Player(models.Model):
    full_name = models.CharField(max_length=50, verbose_name=_('نام '))
    pic = models.ImageField(upload_to='player/', verbose_name=_('عکس '))
    number = models.SmallIntegerField(verbose_name=_('شماره '))
    post = models.CharField(max_length=30, verbose_name=_('پست '))
    age = models.SmallIntegerField(verbose_name=_('سن '))
    goal = models.SmallIntegerField(verbose_name=_(' گل زده '))

    def __str__(self):
        return f"{self.full_name} {self.number}"
