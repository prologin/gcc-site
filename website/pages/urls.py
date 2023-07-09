from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path(
        "legal-notices/",
        views.LegalNoticesView.as_view(),
        name="legal_notices",
    ),
    path("privacy/", views.PrivacyMainView.as_view(), name="privacy"),
    # TODO: Create appropriate pages
    path(
        "privacy-inscription/",
        views.PrivacyView.as_view(),
        name="privacy_inscription",
    ),
    path("privacy-stage/", views.PrivacyView.as_view(), name="privacy_stage"),
    path(
        "privacy-newsletter/",
        views.PrivacyView.as_view(),
        name="privacy_newsletter",
    ),
    path("faq/", views.FAQView.as_view(), name="FAQ"),
]
