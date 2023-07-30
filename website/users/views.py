from typing import Any
import csv

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, RedirectURLMixin
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import resolve_url, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, DeleteView, TemplateView
from django.views.generic.edit import UpdateView

from .forms import (
    AuthLoginForm,
    AuthRegisterForm,
    DeleteUserForm,
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User
from events.models import events, signup

# Extra message tags
TAG_PERSONAL_INFO = "personal_info"
TAG_EMAIL = "email"
TAG_PWD = "pwd"

class UserEditView(LoginRequiredMixin, UpdateView):
    http_method_names = ("post",)
    model = User
    fields = (
        "first_name",
        "last_name",
    )

    def get_object(self, *args, **kwargs):
        return User.objects.get(id=self.request.user.id)

    def get_success_url(self):
        return reverse_lazy("users:account_information") + '#personal-info'

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse_lazy("users:account_information") + '#password'

class ExportUsersCSVView(View):
    model = User

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Application Title', 'Application Description'])

        users = User.objects.all()
        applications = signup.Application.objects.filter(
            user=self.request.user.id
        ).order_by("-created_at")


        for user in users:
            writer.writerow([user.first_name, user.last_name, user.email])


        for application in applications:
            # Add application data to the CSV row
            writer.writerow([application.title, application.description])
        return response

    def get_object(self, *args, **kwargs):
        return User.objects.get(id=self.request.user.id)

class UserDeleteView(DeleteView):
    model = User
    http_method_names = ("post",)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, _("L'utilisateur a été supprimé"))
        return reverse('events:home')

    def delete(self, request, *args, **kwargs):
        # You can add additional checks here if needed before deletion
        return super().delete(request, *args, **kwargs)



class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"

    def post(self, request, *agrs, **kwargs):
        personal_info_form = PersonalInfoForm(request.POST)
        email_form = EmailForm(request.POST)
        password_update_form = PasswordUpdateForm(request.POST)
        notifs_update_form = NotificationsUpdateForm(request.POST)


        if "submit-email" in request.POST:
            # user cannot be None because the page requires login
            user = User.objects.get(id=request.user.id)

            email = request.POST["email"]
            email_validator = EmailValidator()

            try:
                email_validator(email)  # This will raise ValidationError if email is invalid
            except ValidationError:
                messages.warning(
                    request,
                    "L'email est invalide !",
                    extra_tags=TAG_EMAIL,
                )
                return HttpResponseRedirect(reverse("users:account_information") + '#email')

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

            return HttpResponseRedirect(reverse("users:account_information") + '#email')

        elif "submit-notifications" in request.POST:
            return HttpResponse("Notifs update form valid")


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
            "delete_user_form": DeleteUserForm(),
        }


class LoginView(auth_views.LoginView):
    template_name = "users/login.html"
    form_class = AuthLoginForm
    redirect_authenticated_user = True


class RegisterView(RedirectURLMixin, CreateView):
    template_name = "users/register.html"
    form_class = AuthRegisterForm

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
