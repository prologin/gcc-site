from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("about/", views.AboutView.as_view()),
    path("legal-notices/", views.LegalNoticesView.as_view()),
    path("privacy/", views.PrivacyView.as_view()),
]