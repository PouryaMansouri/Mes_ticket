from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

UserAdmin.list_display = ('phone_number', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone_number', 'first_name', 'last_name')
UserAdmin.ordering = ('phone_number',)
UserAdmin.fieldsets[0][1]['fields'] = ('phone_number', 'password')
admin.site.register(User, UserAdmin)


class BaseAdmin(admin.ModelAdmin):
    pass
