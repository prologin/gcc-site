from django.contrib import admin
from . import models


@admin.register(models.Partner)
class PartnersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "enabled",
        "featured",
        "order",
        "website_url",
    )

    list_filter = ("enabled",)
