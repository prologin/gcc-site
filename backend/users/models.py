from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Remove the username field from AbstractUser
    username = None

    email = models.EmailField(
        verbose_name=_("Adresse email"),
        null=False,
        blank=False,
        unique=True,
    )

    newsletter_subscribed = models.BooleanField(
        default=False,
        editable=True,
    )
