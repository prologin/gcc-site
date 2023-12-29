from django.contrib import admin

from . import models


class AddressAdmin(admin.StackedInline):
    model = models.Address
    fields = (
        "street",
        "complement",
        "zip_code",
        "city",
        "country",
        "gg_maps_query",
    )
    extra = 0
    min_num = 1


@admin.register(models.Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address__city")
    fieldsets = (
        (None, {"fields": ("name",)}),
        ("Notes", {"fields": ("private_notes",)}),
    )
    inlines = (AddressAdmin,)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "center", "year", "start_date", "end_date")
    list_filter = ("center", "year")
    ordering = ("-start_date",)

    fieldsets = (
        (None, {"fields": ("name", "center", "year")}),
        (
            "Dates de l'évènement",
            {
                "fields": ("start_date", "end_date"),
            },
        ),
        (
            "Dates d'inscription",
            {"fields": ("signup_start_date", "signup_end_date")},
        ),
        (
            "Informations aux participantes",
            {"fields": ("description", "notes")},
        ),
        ("Documents du stage", {"fields": ("documents",)}),
    )
