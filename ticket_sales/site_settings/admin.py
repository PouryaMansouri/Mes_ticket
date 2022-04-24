from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSetting

admin.site.register(SiteSetting)