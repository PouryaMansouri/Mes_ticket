from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from events.forms import TicketFormSet, TicketForm
from events.models import Event, Ticket


class Index(CreateView):
    model = Ticket
    template_name = 'index.html'
    form_class = TicketForm
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-datetime').all()[:4]
        data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
        }
        context['ticket_forms'] = TicketFormSet(data)
        return context

    def post(self, request, *args, **kwargs):
        formset = TicketFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        tickets = formset.save(commit=False)
        for ticket in tickets:
            ticket.customer = customer
            ticket.save()
        return redirect('events:index')
