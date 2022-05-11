from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, phone_number, **extra_fields):
        """Create a user instance with the given email and password.

                    This is a helper method to create a user instance without saving it
                    to the database.

                    Args:
                        email (str): The user's email address.
                        password (str): The user's password.
                        is_staff (bool): Whether the user is a staff member.
                        is_superuser (bool): Whether the user is a superuser.
                        phone_number (str): The user's phone number.
                        extra_fields (dict): Any extra fields to add to the user.

                    Returns:
                        User: The created user instance.

                    Raises:
                        ValueError: If the given email is not unique.
                """
        if not email:
            raise ValueError(_('users must have an email address'))
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            phone_number=phone_number,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, phone_number=None, **extra_fields):
        """Create and save a regular user with the given email and password.

                    Args:
                        email (str): The user's email address.
                        password (str): The user's password.
                        phone_number (str): The user's phone number.
                        extra_fields (dict): Any extra fields to add to the user.

                    Returns:
                        User: The created user instance.

                    Raises:
                        ValueError: If the given email is not unique.
                """
        return self._create_user(email, password, False, False, phone_number, **extra_fields)

    def create_superuser(self, email, password, phone_number, **extra_fields):
        """Create and save a superuser with the given email and password.

                    Args:
                        email (str): The user's email address.
                        password (str): The user's password.
                        phone_number (str): The user's phone number.
                        extra_fields (dict): Any extra fields to add to the user.

                    Returns:
                        User: The created user instance.

                    Raises:
                        ValueError: If the given email is not unique.
                """
        user = self._create_user(email, password, True, True, phone_number, **extra_fields)
        user.save(using=self._db)
        return user

