from typing import Any

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import RedirectURLMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, TemplateView

from .forms import (
    AuthLoginForm,
    AuthRegisterForm,
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User

# Extra message tags
TAG_PERSONAL_INFO = "personal_info"
TAG_EMAIL = "email"
TAG_PWD = "pwd"


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"

    def post(self, request, *agrs, **kwargs):
        personal_info_form = PersonalInfoForm(request.POST)
        email_form = EmailForm(request.POST)
        password_update_form = PasswordUpdateForm(request.POST)
        notifs_update_form = NotificationsUpdateForm(request.POST)

        if "submit-personal_info" in request.POST:
            # user cannot be None because the page requires login
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            # Update user in the database.
            user.save()

            # Send a message to display
            messages.success(
                request,
                "Informations personnelles mises à jour",
                extra_tags=TAG_PERSONAL_INFO,
            )

            return HttpResponseRedirect(reverse("users:account_information"))

        elif "submit-email" in request.POST:
            # user cannot be None because the page requires login
            user = User.objects.get(id=request.user.id)

            email = request.POST["email"]

            try:
                # Try to find existing account with this email
                match = User.objects.get(email=email)
                # Send a message to display
                messages.warning(
                    request,
                    "Un utilisateur avec cet email existe déjà !",
                    extra_tags=TAG_EMAIL,
                )
            except User.DoesNotExist:
                # Unable to find a user, this is fine
                user.email = email
                # Update user in the database.
                user.save()

                # Send a message to display
                messages.success(
                    request,
                    "Informations personnelles mises à jour",
                    extra_tags=TAG_EMAIL,
                )

            return HttpResponseRedirect(reverse("users:account_information"))

        elif "submit-password" in request.POST:
            url_password = reverse("users:account_information") + "#password"
            # Check if the new password is valid (minimum length, common pwd, etc)
            if not password_update_form.is_valid():
                messages.warning(
                    request,
                    str(password_update_form.errors),
                    extra_tags=TAG_PWD,
                )
                return HttpResponseRedirect(url_password)

            new_pwd = request.POST["new_pwd"]
            new_pwd_ack = request.POST["new_pwd_ack"]

            # Check if the 2 passwords match
            if new_pwd != new_pwd_ack:
                messages.warning(
                    request,
                    _("Les deux mot de passes ne correspondent pas !"),
                    extra_tags=TAG_PWD,
                )
                return HttpResponseRedirect(url_password)

            # user cannot be None because the page requires login
            user = User.objects.get(id=request.user.id)
            current_pwd = request.POST["current_pwd"]

            # Check if new password is the same than current one
            if check_password(new_pwd, user.password):
                messages.warning(
                    request,
                    _("Votre nouveau mot de passe est identique à l'actuel"),
                    extra_tags=TAG_PWD,
                )
                return HttpResponseRedirect(url_password)

            # Check if current password is correct
            if check_password(current_pwd, user.password):
                user.set_password(new_pwd)
                user.save()
                update_session_auth_hash(request, user)
                # Send a message to display
                messages.success(
                    request,
                    _("Votre mot de passe à été mis à jour !"),
                    extra_tags=TAG_PWD,
                )
                return HttpResponseRedirect(url_password)
            else:
                messages.warning(
                    request,
                    _("Votre mot de passe est incorrect."),
                    extra_tags=TAG_PWD,
                )
                return HttpResponseRedirect(url_password)

        elif "submit-notifications" in request.POST:
            return HttpResponse("Notifs update form valid")

        return HttpResponse("nothing")

    def get_context_data(self, **kwargs: Any):
        # Get the request user to prefill the forms
        user = User.objects.get(id=self.request.user.id)

        user_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }

        return {
            "personal_info_form": PersonalInfoForm(user_data),
            "email_form": EmailForm(user_data),
            "password_update_form": PasswordUpdateForm(),
            "notifs_update_form": NotificationsUpdateForm(),
        }


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    form_class = AuthLoginForm
    redirect_authenticated_user = True


class RegisterView(RedirectURLMixin, CreateView):
    template_name = "users/register.html"
    form_class = AuthRegisterForm
    success_url = "/"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        """
        Like for the Login View, prevent the access of logged users to this page
        """
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_default_redirect_url(self):
        if self.success_url:
            return resolve_url(self.success_url)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)
