from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, *args, **kwargs):
        return {}