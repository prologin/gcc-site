# noqa
# pylint: skip-file
"""
Django settings for template project.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

from django_utils.settings.caches import *
from django_utils.settings.common import *
from django_utils.settings.databases import *
from django_utils.settings.logging import *

from django_utils.settings.auth import *  # isort:skip
from django_utils.settings.celery import *  # isort:skip
from django_utils.settings.drf import *  # isort:skip


PROJECT_NAME = "gccsite"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = installed_apps(with_auth=True) + [
    "django_filters",
    "events",
    "partners",
    "users",
]


AUTH_USER_MODEL = "users.User"


MIDDLEWARE = middleware(with_auth=True)

DATABASES = databases(PROJECT_NAME)

ROOT_URLCONF = root_urlconf(PROJECT_NAME)

WSGI_APPLICATION = wsgi_application(PROJECT_NAME)

REST_FRAMEWORK = rest_framework(with_auth=True)

# The default filter backend does not properly set the field types, making all
# query parameters string type.
# Having proper types in the generated OpenAPI file is **extremely** important
# since it will greatly help to use the API.
# REST_FRAMEWORK["DEFAULT_FILTER_BACKENDS"] = ["gccsite.backends.FilterBackend"]
