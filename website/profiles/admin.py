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
                    "street_app",
                    "complement_app",
                    "city_app",
                    "zipcode_app",
                    "country_app",
                )
            },
        ),
        (
            "Responsable légal",
            {
                "fields": (
                    "email_resp",
                    "phone_resp",
                    "street_resp",
                    "complement_resp",
                    "city_resp",
                    "zipcode_resp",
                    "country_resp",
                )
            },
        ),
        (
            "Établissement scolaire",
            {
                "fields": (
                    "school_name",
                    "street_school",
                    "complement_school",
                    "city_school",
                    "zipcode_school",
                    "country_school",
                )
            },
        ),
    )
