from django.urls import path

from . import views

from django.views.decorators.cache import cache_page

app_name = "partners"

urlpatterns = [
    path("partners/", cache_page(60*60)(views.PartnersView.as_view()), name="partners"),
]
