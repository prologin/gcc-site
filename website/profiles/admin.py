from django.contrib import admin

from profiles import models

# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ("email",)
    list_display = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            "Informations participante",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "birth_date",
                    "address",
                )
            },
        ),
        (
            "Responsable légal",
            {
                "fields": (
                    "first_name_resp",
                    "last_name_resp",
                    "email_resp",
                    "phone_resp",
                    "address_resp",
                )
            },
        ),
        (
            "Établissement scolaire",
            {"fields": ("school",)},
        ),
    )
