from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .simplejwt_yasg import (
    DecoratedTokenObtainPairView,
    DecoratedTokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Girls Can Code! API",
        default_version="v1",
        description="API for Girls Can Code! website",
        contact=openapi.Contact(email="info@girlscancode.fr"),
    ),
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/sso/", include("social_django.urls", namespace="social")),
    path(
        "api/v1/token/",
        DecoratedTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/token/refresh/",
        DecoratedTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("api/v1/", include("events.urls", namespace="events")),
    path("api/v1/", include("partners.urls", namespace="partners")),
    path("api/v1/", include("users.urls", namespace="users")),
    # Swagger UI and Redoc URLs
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

# Serve uploaded media when DEBUG is activated
# This is mainly to make the dev environment easier
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
