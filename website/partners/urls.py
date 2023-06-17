from django.urls import path

from . import views

urlpatterns = [
    path("", views.partners_view, name="partners_view"),
    path("featured/", views.partners_view_featured, name="partners_view_featured"),
]