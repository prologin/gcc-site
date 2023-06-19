# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (c) 2022 Association Prologin <association@prologin.org>
# Copyright (c) 2022 Marc 'risson' Schmitt <marc.schmitt@prologin.org>

import logging

from django.contrib.auth.models import Group
from django.db import transaction
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from mozilla_django_oidc.utils import import_from_settings

_logger = logging.getLogger(__name__)


class ProloginOIDCAB(OIDCAuthenticationBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.GroupModel = Group

    def create_user(self, claims):
        email = claims.get("email")

        _logger.debug("Creating user %s", email)

        user = self.UserModel.objects.create_user(email=email)

        self.update_groups(user, claims)

        self.set_permissions(user, claims)

        return user

    def update_user(self, user, claims):
        username = self.get_username(claims)

        _logger.debug("Updating user %s", username)

        user.username = username

        self.set_permissions(user, claims, save=False)

        user.save()

        self.update_groups(user, claims)

        return user

    def update_groups(self, user, claims):
        groups = claims.get("groups")
        user_groups = []

        for group in groups:
            user_group, _ = self.GroupModel.objects.get_or_create(name=group)
            user_groups.append(user_group)
        with transaction.atomic():
            user.groups.clear()
            user.groups.add(*set(user_groups))

    def set_permissions(self, user, claims, save=True):
        roles = claims.get("roles")
        user.is_superuser = "superuser" in roles
        user.is_staff = "staff" in roles
        if save:
            user.save()
