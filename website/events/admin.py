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
        "lat",
        "lng",
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
    )


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "status",
        "event",
    )

    raw_id_fields = (
        "user",
        "event",
    )

    search_fields = (
        "first_name",
        "last_name",
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
            {"fields": ("first_name", "last_name", "dob", "form_answer")},
        ),
        (
            "Responsable légal",
            {"fields": ("phone", "address")},
        ),
        ("Etablissement scolaire", {"fields": ("school",)}),
        (
            "Sélection",
            {
                "fields": ("status",),
            },
        ),
    )


@admin.register(models.ApplicationLabel)
class ApplicationLabelAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    