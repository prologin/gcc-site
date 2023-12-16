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
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Coordonnées",
            {
                "fields": (
                    "phone",
                    "birth_date",
                    "address",
                ),
            },
        ),
        ("Responsable", {"fields": ("responsable",)}),
    )
