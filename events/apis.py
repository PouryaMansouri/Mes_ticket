from rest_framework.generics import CreateAPIView

from events.models import Ticket
from events.serializers import TicketSerializer


class TicketAPI(CreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
