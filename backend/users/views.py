from typing import Any, Dict
from django.views.generic import TemplateView
from .models import User
from .forms import PersonalInfoForm, EmailForm, PasswordUpdateForm, NotificationsUpdateForm

class AccountInformationsView(TemplateView):
  template_name = 'users/AccountInformationsView.html'

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    return {
      'personal_info_form' : PersonalInfoForm(),
      'email_form' : EmailForm(),
      'password_update_form': PasswordUpdateForm(),
      'notifs_update_form': NotificationsUpdateForm()
      }