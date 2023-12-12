from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin

from applications import models


@admin.register(models.Application)
class ApplicationAdmin(FSMTransitionMixin, admin.ModelAdmin):
    list_display = (
        "user",
        "profile",
        "status",
        "event",
    )

    raw_id_fields = (
        "user",
        "event",
    )

    search_fields = (
        "profile__first_name",
        "profile__last_name",
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    list_filter = (
        "status",
        "event",
    )

    fieldsets = (
        (None, {"fields": ("user", "event")}),
        (
            "Informations participante",
            {
                "fields": (
                    "profile",
                    "form_answer",
                )
            },
        ),
        (
            "Sélection",
            {
                "fields": (
                    "status",
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
