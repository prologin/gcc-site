from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import (
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    template_name = "users/AccountInformationsView.html"
    form_classes = {
        "personal_info_form": PersonalInfoForm(),
        "email_form": EmailForm(),
        "password_update_form": PasswordUpdateForm(),
        "notifs_update_form": NotificationsUpdateForm(),
    }

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

                return HttpResponse(
                    f"Updated\n{request.POST['first_name']} {request.POST['last_name']}"
                )

            elif email_form.is_valid():
                print(request.POST["email"])
                return HttpResponse(request.POST["email"])

            elif password_update_form.is_valid():
                return HttpResponse("Password update form valid")

            elif notifs_update_form.is_valid():
                return HttpResponse("Notifs update form valid")

        return HttpResponse("nothing")

    def get_context_data(self, **kwargs: Any):
        return self.form_classes
