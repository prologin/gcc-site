from django.contrib import admin

from . import models

"""
@admin.register(models.Region)
class Region(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "managers")
    autocomplete_fields = ("managers",)
"""


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

    def has_add_permission(self, request):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )

    def has_change_permission(self, request, obj=None):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )

    def has_delete_permission(self, request, obj=None):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "center", "year", "start_date", "end_date")
    list_filter = ("center", "year")
    ordering = ("-start_date",)
    autocomplete_fields = ("managers", "staff")

    fieldsets = (
        (None, {"fields": ("name", "center", "year")}),  # , "region")}),
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
        (
            "Responsable du stage",
            {"fields": ("managers", "staff")},
        ),
        ("Documents du stage", {"fields": ("documents",)}),
    )

    def has_add_permission(self, request, obj=None):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )

    def has_change_permission(self, request, obj=None):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )

    def has_delete_permission(self, request, obj=None):
        return (
            request.user.groups.filter(name="respo-regionaux").exists()
            or request.user.is_superuser
        )
