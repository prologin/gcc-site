from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

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
        (_("Notes"), {"fields": ("private_notes",)}),
    )
    inlines = (AddressAdmin,)


class EventDocumentInlineAdmin(admin.TabularInline):
    model = models.Event.documents.through
    fields = ("document", "display_name", "visibility")
    extra = 0


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "center", "start_date", "end_date")
    list_filter = ("center",)
    ordering = ("-start_date",)
    inlines = (EventDocumentInlineAdmin,)

    fieldsets = (
        (None, {"fields": ("name", "center")}),
        (
            _("Dates de l'évènement"),
            {
                "fields": ("start_date", "end_date"),
            },
        ),
        (
            _("Dates d'inscription"),
            {"fields": ("signup_start_date", "signup_end_date")},
        ),
        (
            _("Formulaires d'inscription"),
            {"fields": ("form",)},
        ),
        (
            _("Informations aux participants"),
            {"fields": ("description", "notes")},
        ),
    )


class QuestionInlineAdmin(admin.TabularInline):
    model = models.Question
    fields = ("order", "text", "type", "mandatory", "answers")
    extra = 0


@admin.register(models.Form)
class FormAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    inlines = (QuestionInlineAdmin,)


class FormAnswerInline(admin.TabularInline):
    model = models.FormAnswer
    fields = ("question", "answer")
    extra = 0


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "owner",
        "status",
        "event",
    )

    raw_id_fields = (
        "owner",
        "event",
    )

    search_fields = (
        "first_name",
        "last_name",
        "owner__username",
        "owner__first_name",
        "owner__last_name",
        "owner__email",
    )

    list_filter = (
        "status",
        "event",
        "labels",
    )

    filter_horizontal = ("labels",)

    fieldsets = (
        (None, {"fields": ("owner", "event")}),
        (
            _("Informations participant"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "dob",
                )
            },
        ),
        (
            _("Sélection"),
            {
                "fields": ("status", "labels"),
            },
        ),
    )

    inlines = (FormAnswerInline,)


@admin.register(models.ApplicationLabel)
class ApplicationLabelAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    search_fields = ("display_name", "admin_name")
