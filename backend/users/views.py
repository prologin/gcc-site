from typing import Any, Dict
from django.views.generic import TemplateView
from .models import User
from .forms import PersonalInfoForm

class AccountInformationsView(TemplateView):
  template_name = 'users/AccountInformationsView.html'

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    return {'form' : PersonalInfoForm()}