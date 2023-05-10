from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name="Adresse email",
        unique=True,
    )

    newsletter_subscribed = models.BooleanField(
        default=False,
        editable=True,
    )
