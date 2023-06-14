from pathlib import Path

from gccsite import env

from .debug import DEBUG

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_secret("DJANGO_SECRET_KEY")

PROBES_IPS = env.get_list("DJANGO_PROBES_IP", ["0.0.0.0/0"])
ALLOWED_HOSTS = env.get_list("DJANGO_ALLOWED_HOSTS", [])
DEFAULT_DOMAIN = ALLOWED_HOSTS[0] if ALLOWED_HOSTS else "app.localhost"
ALLOWED_CIDR_NETS = env.get_list("DJANGO_ALLOWED_CIDR", [])

# A list of the emails who get error notifications.
ADMINS = [(mail, mail) for mail in env.get_list("DJANGO_ADMINS", [])]
MANAGERS = [
    (mail, mail) for mail in env.get_list("DJANGO_MANAGERS", [])
] or ADMINS

# Redirect plain HTTP requests to HTTPS.
SECURE_SSL_REDIRECT = not DEBUG
SECURE_REDIRECT_EXEMPT = env.get_list(
    "DJANGO_SECURE_REDIRECT_EXEMPT", ["^metrics$"]
)

# Avoid transmitting the CSRF cookie over HTTP accidentally.
CSRF_COOKIE_SECURE = not DEBUG

# Avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = not DEBUG

# See https://docs.djangoproject.com/en/4.0/ref/middleware/#referrer-policy
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

PROJECT_NAME = "gccsite"
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "post_office",
    "crispy_forms",
    "crispy_bootstrap5",
    "events",
    "users",
    "pages",
    "gccsite.storage",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gccsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "gccsite" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "gccsite.context_processors.my_context_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "gccsite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# By default, bring back user to home when successfully logging in
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = "/"

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "users.User"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Email settings

DEFAULT_FROM_EMAIL = env.get_string(
    "DJANGO_DEFAULT_FROM_EMAIL", f"noreply@{DEFAULT_DOMAIN}"
)

EMAIL_BACKEND = "post_office.EmailBackend"
POST_OFFICE = {
    "CELERY_ENABLED": True,
    "DEFAULT_PRIORITY": "now",
    "MESSAGE_ID_ENABLED": True,
    "MESSAGE_ID_FQDN": DEFAULT_DOMAIN,
    "MAX_RETRIES": 3,
    "LOG_LEVEL": 1 if not DEBUG else 2,
}
if DEBUG:
    POST_OFFICE["BACKENDS"] = {
        "default": "django.core.mail.backends.console.EmailBackend",
    }
else:
    POST_OFFICE["BACKENDS"] = {
        "default": "django.core.mail.backends.smtp.EmailBackend",
    }
    EMAIL_HOST = env.get_string("DJANGO_SMTP_HOSTNAME", "localhost")
    EMAIL_PORT = env.get_string("DJANGO_SMTP_PORT", 25)
    EMAIL_HOST_USER = env.get_string("DJANGO_SMTP_USER", "")
    EMAIL_HOST_PASSWORD = env.get_secret("DJANGO_SMTP_PASSWORD", "")
    EMAIL_USE_TLS = env.get_bool("DJANGO_SMTP_STARTTLS", False)

# Those are only used to send emails to admins and managers
SERVER_EMAIL = env.get_string("DJANGO_SERVER_EMAIL", DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env.get_string(
    "DJANGO_EMAIL_SUBJECT_PREFIX", "[DJANGO] "
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = (BASE_DIR / "static/",)

AWS_ACCESS_KEY_ID = env.get_secret("S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = env.get_secret("S3_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = env.get_string("S3_BUCKET")
AWS_S3_ENDPOINT_URL = env.get_string("S3_ENDPOINT")
AWS_S3_CUSTOM_DOMAIN = env.get_string("S3_CUSTOM_DOMAIN", "") or None
AWS_S3_URL_PROTOCOL = (
    "https:" if env.get_bool("S3_SECURE_URLS", True) else "http:"
)

AWS_S3_BASE_URL = (f"{AWS_S3_URL_PROTOCOL}//") + (
    AWS_S3_CUSTOM_DOMAIN or f"localhost:8020/{AWS_STORAGE_BUCKET_NAME}"
)

AWS_STATIC_LOCATION = "static"
STATIC_URL = f"{AWS_S3_BASE_URL}/{AWS_STATIC_LOCATION}/"
STATICFILES_STORAGE = "gccsite.storage.backends.StaticStorage"

AWS_PUBLIC_MEDIA_LOCATION = "media/public"
MEDIA_URL = f"{AWS_S3_BASE_URL}/{AWS_PUBLIC_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "gccsite.storage.backends.PublicMediaStorage"

AWS_PRIVATE_MEDIA_LOCATION = "media/private"
PRIVATE_FILE_STORAGE = "gccsite.storage.backends.PrivateMediaStorage"