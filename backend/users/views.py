from typing import Any, Dict

from django.views.generic import TemplateView

from .forms import (
    EmailForm,
    NotificationsUpdateForm,
    PasswordUpdateForm,
    PersonalInfoForm,
)
from .models import User


class AccountInformationsView(TemplateView):
    template_name = "users/AccountInformationsView.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return {
            "personal_info_form": PersonalInfoForm(),
            "email_form": EmailForm(),
            "password_update_form": PasswordUpdateForm(),
            "notifs_update_form": NotificationsUpdateForm(),
        }
