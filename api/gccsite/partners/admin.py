from django.contrib import admin

from . import models


@admin.register(models.Partner)
class PartnersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "enabled",
        "featured",
        "is_on_front_page",
        "order",
        "website_url",
    )

    list_filter = (
        "enabled",
        "featured",
        "is_on_front_page",
    )
