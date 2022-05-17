from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from events.forms import TicketForm
from events.models import Event
from players.models import Player

from django.views import View
from .models import Ticket


class Index(FormView):
    form_class = TicketForm
    template_name = 'index.html'
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = Player.objects.all()[:4]
        event = Event.objects.last()
        context['players'] = players
        context['event'] = event
        context['event_date'] = event.str_event_time
        return context


class TicketView(LoginRequiredMixin, View):
    def get(self, request):
        phone = request.user.phone_number
        tickets = Ticket.objects.filter(phone=phone)
        return render(request, 'ticket/show_ticket.html', {'tickets': tickets})
