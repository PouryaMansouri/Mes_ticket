from django.contrib import admin

from core.admin import BaseAdmin
from site_settings.models import SiteSetting


class SiteSettingAdmin(BaseAdmin):
    list_display = ['site_name', 'contact_phone', 'contact_email']


admin.site.register(SiteSetting, SiteSettingAdmin)
