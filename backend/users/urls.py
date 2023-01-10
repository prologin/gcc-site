from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "users"

router = routers.SimpleRouter()
router.register("", views.UserViewset, basename="users")

urlpatterns = [
    path("users/", include(router.urls)),
    path("users/me/", views.UserMeView.as_view(), name="me"),
]
