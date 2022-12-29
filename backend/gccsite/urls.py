from django.urls import include, path
from django_utils.urls import default, drf

urlpatterns = (
    default.urlpatterns()
    + drf.urlpatterns(with_auth=True)
    + [
        path("rest/v1/", include("events.urls", namespace="events")),
        path("rest/v1/", include("partners.urls", namespace="partners")),
        path("rest/v1/", include("users.urls", namespace="users")),
    ]
)
