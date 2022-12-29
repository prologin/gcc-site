from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UpstreamUserAdmin
from django.contrib.auth.decorators import login_required

from . import models

admin.site.login = login_required(admin.site.login)


@admin.register(models.User)
class UserAdmin(UpstreamUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Informations personnelles",
            {"fields": ("first_name", "last_name", "email")},
        ),
        (
            "Adresse postale",
            {"fields": ("address", "city", "zip_code", "country")},
        ),
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
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
