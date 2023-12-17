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

    raw_id_fields = (
        "profile",
        "event",
    )

    search_fields = (
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__user__email",
        "profile__first_name",
        "profile__last_name",
        "profile__email",
    )

    list_filter = (
        "status",
        "event",
    )

    fieldsets = (
        (None, {"fields": ("profile", "event")}),
        (
            "Informations participante",
            {"fields": ("form_answer",)},
        ),
        (
            "Sélection",
            {
                "fields": (
                    "status",
                    "notes",
                    # TODO: Add a "nb_participation" property to the profile model
                ),
            },
        ),
    )

    ordering = ["-created_at"]

    fsm_field = ["status"]
    readonly_fields = ["status", "created_at"]


@admin.register(models.ApplicationLabel)
class ApplicationLabelAdmin(admin.ModelAdmin):
    search_fields = ("title",)
