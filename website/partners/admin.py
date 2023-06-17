from django.contrib import admin

# Register your models here.


from .models import Partner
admin.site.register(Partner, admin.ModelAdmin)

class PartnerAdmin(Partner):
    ordering = ("name",)
    list_display = ("name", "description", 'website_url',)
    search_fields = ("name", "website_url", )

    