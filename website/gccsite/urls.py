from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("", include("pages.urls")),
    path("", include("users.urls")),
    path("", include("partners.urls")),
    path("rest/auth/oidc/", include("mozilla_django_oidc.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
