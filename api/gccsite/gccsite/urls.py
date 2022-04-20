from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/sso/", include("social_django.urls", namespace="social")),
    path("api/v1/events/", include("events.urls", namespace="events")),
    path("api/v1/partners/", include("partners.urls", namespace="partners")),
    path("api/v1/users/", include("users.urls", namespace="users")),
]
