from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import (
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User


class AccountInformationsView(LoginRequiredMixin, TemplateView):
    login_url = "/login/"
    # redirect_field_name = 'redirect_to'
    template_name = "users/AccountInformationsView.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        user = User.objects.get(id=self.request.user.id)
        user_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_date,
            "street": user.address.street,
            "zip_code": user.address.zip_code,
            "city": user.address.city,
            "country": user.address.country,
        }

        return {
            "personal_info_form": PersonalInfoForm(user_data),
            "email_form": EmailForm(),
            "password_update_form": PasswordUpdateForm(),
            "notifs_update_form": NotificationsUpdateForm(),
        }
