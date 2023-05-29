from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UpstreamUserAdmin

from . import models


@admin.register(models.User)
class UserAdmin(UpstreamUserAdmin):
    # Override UpstreamUserAdmin's ordering which depends on removed "username"
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Informations personnelles",
            {"fields": ("first_name", "last_name")},
        ),
        ("Paramètres newsletter", {"fields": ("newsletter_subscribed",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Dates importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2"),
            },
        ),
    )
