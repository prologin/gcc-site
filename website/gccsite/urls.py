from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("", include("events.urls", namespace="events")),
    path("", include("pages.urls", namespace="pages")),
]
