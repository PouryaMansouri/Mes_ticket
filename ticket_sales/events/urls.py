from django.urls import path

from events.apis import TicketAPI
from events.views import Index, TicketView

app_name = 'events'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('ticket-api', TicketAPI.as_view(), name='ticket-api'),
    path('ticket-history', TicketView.as_view(), name='ticket-history')
]
