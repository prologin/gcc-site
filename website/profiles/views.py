from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.http import (
    HttpResponseBadRequest,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView

from profiles.forms import ProfileCreationForm
from profiles.models import Profile
from profiles.utils import (
    check_profile_email_token,
    generate_profile_email_token,
)


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
            messages.success(
                request,
                "Votre profil a été enregistré ! Confirmez les adresses email renseignées en cliquant sur le lien envoyé dans le mail envoyé à chacunes des adresses",
            )

            return self.form_valid(form)

    def form_valid(self, form):
        profile = form.save()

        # Do not send confirmation email if it is the same as the user account email
        if profile.email == self.request.user.email:
            profile.email_confirmed = True
        else:
            self.send_profile_email_confirmation(profile, "email")

        if profile.email_resp == self.request.user.email:
            profile.email_resp_confirmed = True
        elif profile.email != profile.email_resp:
            # Do not send 2 emails to the same address
            self.send_profile_email_confirmation(profile, "email_resp")

        return HttpResponseRedirect(self.success_url)

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw.update({"user": self.request.user})
        return kw

    def send_profile_email_confirmation(self, profile: Profile, field: str):
        current_site = get_current_site(self.request)
        subject = "Confirmez votre email de profil sur Girls Can Code!"
        email = getattr(profile, field)
        request_id = urlsafe_base64_encode(
            force_bytes(f"{profile.id}|{email}")
        )
        token = generate_profile_email_token(profile, field)

        activation_link = "{0}/profiles/email-confirm/{1}/{2}".format(
            current_site, request_id, token
        )

        email_from = settings.DEFAULT_FROM_EMAIL
        message = render_to_string(
            template_name="profiles/mails/profile_email_activation_link.txt",
            context={
                "firstname": profile.first_name,
                "lastname": profile.last_name,
                "link": activation_link,
            },
        )
        send_mail(subject, message, email_from, [email])


class ProfileListView(LoginRequiredMixin, ListView):
    template_name = "profiles/profiles_list.html"
    model = Profile

    def get_queryset(self):
        profiles = super().get_queryset().filter(user_id=self.request.user.id)
        return profiles


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profiles_detail.html"

    def dispatch(self, request, *args, **kwargs):
        profile_id = self.kwargs.get("pk")
        profile = Profile.objects.get(id=profile_id)

        # Prevent user from accessing other users' profiles
        if request.user != profile.user:
            raise PermissionDenied()

        super().dispatch(request, *args, **kwargs)


class DeleteProfileView(LoginRequiredMixin, View):
    http_method_names = ("post",)

    def post(self, request, *args, **kwargs):
        redirect_url = reverse("profiles:profiles_list")

        profile_id = self.kwargs.get("pk")
        profile = Profile.objects.get(id=profile_id)

        # Prevent user from accessing other users' profiles
        if request.user != profile.user:
            raise PermissionDenied()

        if not profile:
            return HttpResponseBadRequest("Bad request")

        profile.delete()

        messages.success(request, "Le profil a été supprimé")
        return HttpResponseRedirect(redirect_url)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Invalid method")


class ProfileConfirmEmailView(View):
    def get(self, request, requestidb64, token):
        (profile_id, email) = (
            urlsafe_base64_decode(requestidb64).decode().split("|")
        )

        profile = get_object_or_404(Profile, id=profile_id)

        # Check token:
        (valid, email_field) = check_profile_email_token(profile, token)
        if not valid:
            messages.error(request, "La confirmation a échoué")
            return HttpResponseRedirect(reverse_lazy("profiles:profiles_list"))

        # There us a mismatch between profile and email
        if getattr(profile, email_field) != email:
            messages.error(request, "La confirmation a échoué")
            return HttpResponseRedirect(reverse_lazy("profiles:profiles_list"))

        # The email was already validated
        confirmed_field = f"{email_field}_confirmed"
        if getattr(profile, confirmed_field):
            messages.error(request, "Cette adresse email a déjà été confirmée")
            return HttpResponseRedirect(reverse_lazy("profiles:profiles_list"))

        setattr(profile, confirmed_field, True)
        if profile.email == profile.email_resp:
            profile.email_resp_confirmed = True
        profile.save()

        messages.success(request, "Votre adresse email a été activée")
        return HttpResponseRedirect(reverse_lazy("profiles:profiles_list"))
