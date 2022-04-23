from django.urls import reverse_lazy
from django.views.generic import FormView

from events.forms import TicketForm
from events.models import Ticket, Event


class Index(FormView):
    form_class = TicketForm
    template_name = 'index.html'
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_event'] = Event.objects.first().id
        return context


