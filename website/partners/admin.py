from django.contrib import admin

from . import models


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    ordering = ("name",)
    list_display = (
        "name",
        "status",
        "website_url",
    )
    search_fields = (
        "name",
        "website_url",
    )

    fieldsets = (
        (
            "Informations sur le partenaire",
            {
                "fields": (
                    "name",
                    "description",
                    "website_url",
                    "logo",
                )
            },
        ),
        (
            "Status du partenaire",
            {"fields": ("status",)},
        ),
    )
