from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register("events", views.EventViewset, basename="events")
router.register("attendees", views.AttendeeViewset, basename="attendees")

app_name = "events"

urlpatterns = [
    path("", include(router.urls)),
]
