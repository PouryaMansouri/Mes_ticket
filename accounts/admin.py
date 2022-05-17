from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'is_staff', 'national_code')
    list_filter = ('date_joined', 'is_staff')
    search_fields = ('email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
    )
