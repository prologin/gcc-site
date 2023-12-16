from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

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
            address = form.clean_address()

            address_resp = form.clean_address_resp()

            school = form.clean_school_info()

            profile = Profile.objects.create(
                user=self.request.user,
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                birth_date=form.cleaned_data["birth_date"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                address=address,
                first_name_resp=form.cleaned_data["first_name_resp"],
                last_name_resp=form.cleaned_data["last_name_resp"],
                email_resp=form.cleaned_data["email_resp"],
                phone_resp=form.cleaned_data["phone"],
                address_resp=address_resp,
                school=school,
            )

            messages.success(request, "Votre profil a été enregistré !")

            return HttpResponseRedirect(self.success_url)


class ProfileListView(LoginRequiredMixin, ListView):
    template_name = "profiles/profiles_list.html"
    model = Profile

    def get_queryset(self):
        profiles = super().get_queryset()

        return profiles


class ProfileDetailView(DetailView):
    template_name = ""
