# Copyright (C) <2019> Association Prologin <association@prologin.org>
# SPDX-License-Identifier: GPL-3.0+

from .common import *
import os

# You can use $ pwgen -y 64
SECRET_KEY = 'CHANGEME'

# SECURITY/PERFORMANCE WARNING: don't run with DEBUG turned on in production!
DEBUG = True

SESSION_COOKIE_NAME = 'sessionid_gcc'

ALLOWED_HOSTS = ['127.0.0.1', '::1', 'localhost', 'testserver']
INTERNAL_IPS = ALLOWED_HOSTS

SITE_HOST = "localhost:8001"

# Repository paths
ARCHIVES_REPOSITORY_PATH = os.path.join(PROJECT_ROOT_DIR, '..', 'archives')

# OAuth client
OAUTH_ENDPOINT = 'http://localhost:8000/user/auth'
OAUTH_SECRET = 'CHANGEME'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'gcc'}
}

# Logging
# https://docs.djangoproject.com/en/1.7/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler'}
    },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': True}
    },
}


# Email
# Run debug server with:
#   $ make stmpserver

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False


# Recaptcha

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
