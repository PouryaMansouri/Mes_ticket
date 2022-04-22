from django import forms
from django.forms import modelformset_factory

from events.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


TicketFormSet = modelformset_factory(Ticket, fields=('full_name', 'phone', 'national_code', 'event'), extra=1)
