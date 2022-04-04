from django.urls import path

from events.views import Index

app_name = 'events'
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
