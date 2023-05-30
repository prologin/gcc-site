from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls", namespace='events')),
    path("", include("pages.urls", namespace='pages')),
]

handler404 = "pages.views.error_404_view"