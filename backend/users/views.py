from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import (
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User

# Extra message tags
TAG_PERSONAL_INFO = "personal_info"
TAG_EMAIL = "email"


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"

    def post(self, request, *agrs, **kwargs):
        if request.method == "POST":
            personal_info_form = PersonalInfoForm(request.POST)
            email_form = EmailForm(request.POST)
            password_update_form = EmailForm(request.POST)
            notifs_update_form = EmailForm(request.POST)

            if personal_info_form.is_valid():
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

                return HttpResponseRedirect(
                    reverse("users:account_information")
                )

            elif email_form.is_valid():
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

                return HttpResponseRedirect(
                    reverse("users:account_information")
                )

            elif password_update_form.is_valid():
                return HttpResponse("Password update form valid")

            elif notifs_update_form.is_valid():
                return HttpResponse("Notifs update form valid")

        return HttpResponse("nothing")

    def get_context_data(self, **kwargs: Any):
        # Get the request user to prefill the forms
        user = User.objects.get(id=self.request.user.id)

        user_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_date,
            "email" : user.email,
        }

        return {
            "personal_info_form": PersonalInfoForm(user_data),
            "email_form": EmailForm(user_data),
            "password_update_form": PasswordUpdateForm(),
            "notifs_update_form": NotificationsUpdateForm(),
        }
