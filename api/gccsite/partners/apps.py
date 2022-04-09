from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PartnersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "partners"
    label = "partners"
    verbose_name = _("Partners")
