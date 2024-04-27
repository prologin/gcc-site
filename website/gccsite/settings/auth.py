# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2022 Association Prologin <association@prologin.org>
# Copyright (c) 2022 Marc 'risson' Schmitt <marc.schmitt@prologin.org>


from gccsite import env

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.open_id_connect.OpenIdConnectAuth",
]

LOGIN_URL = "/login"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/logout/"
LOGIN_ERROR_URL = "/"

# OIDC

SOCIAL_AUTH_OIDC_OIDC_ENDPOINT = env.get_string("OIDC_OP_CONFIG_URL")
OIDC_RP_SCOPES = " ".join(["openid", "email", "profile", "roles"])


SOCIAL_AUTH_OIDC_KEY = env.get_secret("OIDC_RP_CLIENT_ID")
SOCIAL_AUTH_OIDC_SECRET = env.get_secret("OIDC_RP_CLIENT_SECRET")

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "gccsite.auth.auth_pipeline.map_groups",
    "social_core.pipeline.user.user_details",
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ["first_name", "email"]

ALLOWED_GROUPS = ["staff"]
STAFF_GROUPS = ["respos-reginaux", "bureau", "roots"]
SUPERUSER_GROUPS = ["bureau", "roots"]
