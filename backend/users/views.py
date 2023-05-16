from typing import Any, Dict

from django.contrib import messages

# password check
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
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
TAG_PWD = "pwd"


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"

    def post(self, request, *agrs, **kwargs):
        if request.method == "POST":
            personal_info_form = PersonalInfoForm(request.POST)
            email_form = EmailForm(request.POST)
            password_update_form = PasswordUpdateForm(request.POST)
            notifs_update_form = NotificationsUpdateForm(request.POST)

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
                # user cannot be None because the page requires login
                user = User.objects.get(id=request.user.id)
                current_pwd = request.POST["current_pwd"]

                # check if currect_pwd == pwd
                if check_password(current_pwd, user.password):
                    new_pwd = request.POST["new_pwd"]

                    # check if the 2 new passord are the same
                    if new_pwd == request.POST["new_pwd_ack"]:
                        user.set_password(new_pwd)
                        user.save()
                        update_session_auth_hash(request, user)
                        # Send a message to display
                        messages.success(
                            request,
                            "Votre mot de passe à été changé !",
                            extra_tags=TAG_PWD,
                        )
                    else:
                        # Send a Warning to display
                        messages.warning(
                            request,
                            "Les deux mot de passes ne correspondent pas !",
                            extra_tags=TAG_PWD,
                        )
                else:
                    # Send a Warning to display
                    messages.warning(
                        request,
                        "Votre mot de passe n'est pas bon !",
                        extra_tags=TAG_PWD,
                    )

                return HttpResponseRedirect(
                    reverse("users:account_information")
                )

            elif notifs_update_form.is_valid():
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
