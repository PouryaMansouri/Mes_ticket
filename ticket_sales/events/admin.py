from core.admin import BaseAdmin
from events.models import Event, Team
from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

# you need import this for adding jalali calander widget
import django_jalali.admin as jadmin


class EventAdmin(BaseAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Team)
