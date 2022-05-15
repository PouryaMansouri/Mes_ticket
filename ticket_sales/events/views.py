from django.urls import reverse_lazy
from django.views.generic import FormView

from events.forms import TicketForm
from events.models import Event
from player.models import Player


class Index(FormView):
    form_class = TicketForm
    template_name = 'index.html'
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = Player.objects.filter(goal__gte=3)
        event = Event.objects.last()
        context['players'] = players
        context['event'] = event
        context['event_date'] = event.str_event_time
        return context
