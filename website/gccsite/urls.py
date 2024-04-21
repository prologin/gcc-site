from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("", include("pages.urls")),
    path("", include("users.urls")),
    path("", include("partners.urls")),
    path("", include("applications.urls")),
    path("", include("profiles.urls")),
    path("", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
