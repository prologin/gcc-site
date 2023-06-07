from django.views.generic import TemplateView

from .models import events


class HomePageView(TemplateView):
    template_name = "events/home.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx["open_events"] = events.Event.objects.get_open_events()
        return ctx
