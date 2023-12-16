from django.urls import include, path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path(
        "profiles/create",
        views.CreateProfileView.as_view(),
        name="profiles_create",
    ),
]
