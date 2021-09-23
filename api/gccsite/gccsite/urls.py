from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/sso/", include("social_django.urls", namespace="social")),
    path("api/eventsd/events/", include("eventsd.events.urls")),
    path("api/eventsd/users/", include("eventsd.users.urls")),
    path("api/eventsd/sponsors/", include("eventsd.sponsors.urls")),
]
