from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView

from profiles.forms import ProfileCreationForm
from profiles.models import Profile

# Create your views here.


class CreateProfileView(LoginRequiredMixin, CreateView):
    template_name = "profiles/create_profiles.html"
    form_class = ProfileCreationForm
    success_url = reverse_lazy("profiles:profiles_list")  # TODO: Update this

    def post(self, request, *args, **kwargs):
        self.object = None

        form = self.get_form()

        if not form.is_valid():
            messages.warning(
                request,
                str(form.errors),
            )
            return self.form_invalid(form)
        else:
            messages.success(request, "Votre profil a été enregistré !")
            return self.form_valid(form)

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw.update({"user": self.request.user})
        return kw


class ProfileListView(LoginRequiredMixin, ListView):
    template_name = "profiles/profiles_list.html"
    model = Profile

    def get_queryset(self):
        profiles = super().get_queryset().filter(user_id=self.request.user.id)
        return profiles


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profiles_detail.html"


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, _("Le profil a été supprimé"))
        return reverse("profiles:profiles")

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
