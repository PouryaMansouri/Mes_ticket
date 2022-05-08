from django.contrib.auth.models import UserManager


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)

    # TODO: change manager -> add ValueError for null fields
    # TODO: create instance of user and set password and save instance
    # TODO: add is_staff=True for superuser
