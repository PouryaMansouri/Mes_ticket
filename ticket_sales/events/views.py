from django.views.generic import TemplateView

from events.models import Event


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-datetime').all()[:4]
        return context
