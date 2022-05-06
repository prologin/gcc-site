from .dev import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prologin",
        "USER": "prologin",
        "PASSWORD": "CHANGE_ME",
        "HOST": "gccsite-db",
    }
}
