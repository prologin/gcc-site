from django.shortcuts import render

from profiles.forms import ProfileCreationForm

from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator

from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/profile_create.html"
    form_class = ProfileCreationForm

    @method_decorator(csrf_protect)
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        values = self.form_class(request.POST)
        if not values.is_valid():
            return HttpResponse(values.errors.as_json(), status=400)

        profile = values.save(commit=False)
        profile.owner = request.user;
        profile.save()

        return HttpResponse(status=201)