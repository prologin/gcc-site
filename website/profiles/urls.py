from django.urls import include, path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path(
        "profiles/create",
        views.CreateProfileView.as_view(),
        name="profiles_create",
    ),
    path(
        "profiles",
        views.ProfileListView.as_view(),
        name="profiles_list",
    ),
    path(
        "profiles/<int:id>",
        views.ProfileDetailView.as_view(),
        name="profile_detail",
    ),
]
