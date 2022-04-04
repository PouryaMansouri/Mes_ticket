from django.db import models

from core.models import BaseModel, User
from django.utils.translation import gettext_lazy as _


class Customer(BaseModel):
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
