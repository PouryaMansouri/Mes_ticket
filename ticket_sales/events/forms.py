from django import forms

from events.models import Ticket, Event


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['full_name', 'phone', 'national_code']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['event'].widget = forms.HiddenInput()
    #
    # def full_clean(self):
    #     cleaned_data = super().full_clean()
    #     self.instance.event = Event.objects.first()
    #     return cleaned_data

