from django.urls import path

from profiles import views

app_name = "profiles"

urlpatterns = [
    path(
        "profiles/create/",
        views.CreateProfileView.as_view(),
        name="profiles_create",
    ),
    path(
        "profiles/",
        views.ProfileListView.as_view(),
        name="profiles_list",
    ),
    path(
        "profiles/<int:pk>/",
        views.ProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profiles/<int:pk>/delete/",
        views.DeleteProfileView.as_view(),
        name="profile_delete",
    ),
]
