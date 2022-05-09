from .common import *  # noqa

# Django secret key
SECRET_KEY = "CHANGE_ME"

DEBUG = True

ALLOWED_HOSTS = ["*"]

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

SOCIAL_AUTH_PROLOGIN_KEY = "CHANGE_ME"
SOCIAL_AUTH_PROLOGIN_SECRET = "CHANGE_ME"

AWS_S3_ENDPOINT_URL = "CHANGE_ME"
AWS_STORAGE_BUCKET_NAME = "gcc-site-dev"
AWS_ACCESS_KEY_ID = "CHANGE_ME"
AWS_SECRET_ACCESS_KEY = "CHANGE_ME"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[{asctime}] ({levelname}) {module} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
