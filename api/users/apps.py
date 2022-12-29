from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = "users"
    name = "users"
    verbose_name = "Utilisateurs"