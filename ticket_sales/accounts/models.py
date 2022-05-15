from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """This is the User model that is used for authentication

       In this case user login with Email and password and
       the username is the email.Because this model is inherited
       from the AbstractBaseUser model, it has some fields that are
       required to overwrite(like last_login, date_joined, etc)

       Attributes:
           email (str): The email of the user
           password (str): The password of the user
           username (str): The username of the user
           first_name (str): The first name of the user
           last_name (str): The last name of the user
           phone_number (str): The phone number of the user
           is_staff (bool): The staff status of the user
           is_active (bool): The active status of the user
           is_superuser (bool): The superuser status of the user
           last_login (datetime): The last login of the user
           date_joined (datetime): The date joined of the user
           groups (QuerySet): The groups of the user
           user_permissions (QuerySet): The user permissions of the user
           update_date (datetime): The date of the last update

       Methods:
           __str__ (self): Returns the string representation of the user
           get_full_name (self): Returns the full name of the user
           get_short_name (self): Returns the short name of the user
       """

    # properties
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("نام"), )
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("نام خانوادگی"), )
    email = models.EmailField(unique=True, verbose_name=_("ایمیل"), )
    phone_number = models.CharField(unique=True,max_length=20, blank=True, null=True, verbose_name=_("شماره موبایل"), )
    national_code = models.CharField(max_length=10 ,unique=True, verbose_name=_('کدملی'), blank=True, null=True )
    # auth fields
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.'),
    )
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ بروزرسانی'), )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ پیوستن'), )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'national_code', 'first_name', 'last_name']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['id']
        db_table = 'user'

    def __str__(self):
        """Returns the string representation of the user

                Returns:
                    str: The string representation of the user
                """
        return self.email

    def get_short_name(self):
        """Returns the short name of the user

                   if the first name is not set, returns the email

               Returns:
                   str: The short name of the user
               """
        if self.first_name:
            return self.first_name
        return self.email

    def get_full_name(self):
        """Returns the full name of the user
                    first name + last name with a space in between

                Returns:
                    str: The full name of the user
                """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def username(self) -> str:
        """Returns the username of the user"""
        return self.email

    def clean(self):
        """Cleans the user

                    This method is called before saving the user,
                    it normalizes the email and phone number

                    Raises:
                        ValidationError: If the email is not valid
                        ValidationError: If the phone number is not valid
                """
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        # TODO: implement
        # return reverse("user:detail", kwargs={"pk": self.pk})
        return None
