from django.template.response import SimpleTemplateResponse
from django.views.generic import TemplateView


def error_404_view(request, exception):
    response = SimpleTemplateResponse("pages/404.html")
    response.status_code = 404
    return response

from gccsite.context_processors import my_context_processor


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, *args, **kwargs):
        return {}


class LegalNoticesView(TemplateView):
    template_name = "pages/legal_notices.html"

    def get_context_data(self, *args, **kwargs):
        return {}


class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"

    def get_context_data(self, *args, **kwargs):
        return {}
