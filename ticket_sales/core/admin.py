from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User

UserAdmin.list_display = ('phone', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name')
UserAdmin.ordering = ('phone',)
UserAdmin.fieldsets[0][1]['fields'] = ('phone', 'password')
admin.site.register(User, UserAdmin)


class BaseAdmin(admin.ModelAdmin):
    pass
