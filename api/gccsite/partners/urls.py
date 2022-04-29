from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "partners"

router = routers.SimpleRouter()
router.register("", views.PartnerViewset, basename="partners")

urlpatterns = [
    path("partners/", include(router.urls)),
]
