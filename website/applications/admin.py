from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin

from applications import models


@admin.register(models.Application)
class ApplicationAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        "profile",
        "status",
        "event",
    )

    raw_id_fields = ("event",)

    search_fields = ()

    list_filter = (
        "status",
        "event",
    )

    fieldsets = (
        (None, {"fields": ("event",)}),
        (
            "Sélection",
            {
                "fields": (
                    "status",
                    "nb_participations",
                    "notes",
                ),
            },
        ),
    )

    fsm_field = ["status"]
    readonly_fields = ["status"]


@admin.register(models.ApplicationLabel)
class ApplicationLabelAdmin(admin.ModelAdmin):
    search_fields = ("title",)
