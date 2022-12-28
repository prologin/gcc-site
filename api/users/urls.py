from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("users/me/", views.UserMeView.as_view(), name="me"),
]
