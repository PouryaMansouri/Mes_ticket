from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name','age', 'number')
    search_fields = ('full_name', 'post')
    list_filter = ('post',)
