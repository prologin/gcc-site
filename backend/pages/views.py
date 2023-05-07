from django.views.generic import TemplateView
from gccsite.context_processors import my_context_processor

class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, *args, **kwargs):
        return {}

class LegalNoticesView(TemplateView):
    template_name = 'pages/legal_notices.html'

    def get_context_data(self, *args, **kwargs):
        return my_context_processor(None)