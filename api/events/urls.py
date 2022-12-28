from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register("events", views.EventViewset, basename="events")
router.register("forms", views.FormViewset, basename="forms")
router.register(
    "applications", views.ApplicationViewset, basename="applications"
)

app_name = "events"

urlpatterns = [
    path("", include(router.urls)),
]
