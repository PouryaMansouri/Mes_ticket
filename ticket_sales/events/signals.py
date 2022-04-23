from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Ticket


@receiver(post_save, sender=Ticket)
def my_handler(sender, **kwargs):
    print(sender)
    print('sender'*100)
