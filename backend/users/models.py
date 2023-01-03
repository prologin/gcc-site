from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    address = models.TextField(
        max_length=1000,
        verbose_name="Adresse",
        null=True,
        blank=True,
    )

    city = models.CharField(
        verbose_name="Ville",
        max_length=150,
        null=True,
        blank=True,
    )

    zip_code = models.CharField(
        verbose_name="Code Postal",
        max_length=20,
        null=True,
        blank=True,
    )

    country = models.CharField(
        verbose_name="Pays",
        max_length=64,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name="Adresse email",
        unique=True,
    )

    def has_complete_address(self):
        return not any(
            f is None
            for f in (
                self.address,
                self.city,
                self.zip_code,
                self.country,
            )
        )

    class Meta:
        permissions = [("can_review_applications", "Can review the applications to a camps")]