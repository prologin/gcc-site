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


class EventDocumentInlineAdmin(admin.TabularInline):
    model = models.Event.documents.through
    fields = ("document", "display_name", "visibility")
    extra = 0


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "camps_type" ,"center", "start_date", "end_date")
    list_filter = ("camps_type","center")
    ordering = ("-start_date",)
    inlines = (EventDocumentInlineAdmin,)

    fieldsets = (
        (None, {"fields": ("name", "camps_type", "center")}),
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
            "Formulaires d'inscription",
            {"fields": ("form",)},
        ),
        (
            "Informations aux participantes",
            {"fields": ("description", "notes")},
        ),
    )


@admin.register(models.Form)
class FormAdmin(admin.ModelAdmin):
    search_fields = ("name",)


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
        "labels",
    )

    filter_horizontal = ("labels",)

    fieldsets = (
        (None, {"fields": ("user", "event")}),
        (
            "Informations participante",
            {"fields": ("first_name", "last_name", "dob", "form_answer")},
        ),
        (
            "Sélection",
            {
                "fields": ("status", "labels"),
            },
        ),
    )


@admin.register(models.ApplicationLabel)
class ApplicationLabelAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ("display_name", "admin_name")
