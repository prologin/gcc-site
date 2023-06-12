from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "account-info",
        views.AccountInformationsView.as_view(),
        name="account_information",
    ),
    path(
        "update-user-info",
        views.UserEditView.as_view(),
        name="update_user_info",
    ),
    path(
        "update-user-password",
        views.UserPasswordChangeView.as_view(),
        name="update_user_password",
    ),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
]
