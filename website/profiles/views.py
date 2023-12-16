from django.shortcuts import render

from profiles.forms import ProfileCreationForm

from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator

from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profiles.html"
    form_class = ProfileCreationForm
