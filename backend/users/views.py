from django.views.generic import TemplateView
from .models import User

class AccountInformationsView(TemplateView):
  template_name = 'users/AccountInformationsView.html'