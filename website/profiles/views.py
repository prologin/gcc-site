from django.conf import settings
from django.views.generic.edit import CreateView

from profiles.forms import ProfileCreationForm

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profiles.html"
    form_class = ProfileCreationForm
    success_url = settings.LOGIN_REDIRECT_URL  # TODO: Update this
