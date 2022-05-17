from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from events import validators


class BaseModel(models.Model):
    """
        BaseModel class for all models

        Attributes:
            created_at (models.DateTimeField): Date and time of creation
            updated_at (models.DateTimeField): Date and time of last update
            is_deleted (models.BooleanField): True if the object is deleted


        methods:
           logical_delete(self): logical delete of the object
           logical_restore(self): logical restore of the object


        """

    # Date and time of creation of the object in the database (auto_now_add=True)
    # Date and time of last update of the object in the database (auto_now=True)
    # True if the object is deleted (is_deleted=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('Update at'))
    is_deleted = models.BooleanField(default=False, verbose_name=_('Is deleted'))

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def logical_delete(self) -> None:
        """ logical delete of the object """
        self.is_deleted = True
        self.save()

    def logical_restore(self) -> None:
        """ logical restore of the object """
        self.is_deleted = False
        self.save()


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
