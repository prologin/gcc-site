from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path(
        "account-info",
        views.AccountInformationsView.as_view(),
        name="account_information",
    ),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
