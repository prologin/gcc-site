from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("", include("pages.urls")),
]

handler404 = "pages.views.error_404_view"