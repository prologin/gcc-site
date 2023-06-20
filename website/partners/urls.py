from django.urls import path

from . import views

app_name = "partners"

urlpatterns = [
    path("partners/", views.PartnersView.as_view(), name="partners"),
]
