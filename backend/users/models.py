from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    class Meta:
        verbose_name_plural = "Addresses"

    street = models.TextField()
    zip_code = models.TextField(max_length=5)
    city = models.TextField()
    country = CountryField("Pays", default="FR")

    def __str__(self):
        return (
            f"{self.street}\n{self.zip_code}, {self.city}\n{self.country.name}"
        )

    @classmethod
    def get_default_address(_):
        return Address.objects.get_or_create(
            id=1, street="14-16 rue Voltaire", city="El KB"
        )[0].pk


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(
        null=False,
        blank=False,
        verbose_name="Adresse email",
        unique=True,
    )

    address = models.ForeignKey(
        "Address",
        on_delete=models.CASCADE,
        default=Address.get_default_address,
    )

    birth_date = models.DateField("Date de naissance")

    newsletter_subscribed = models.BooleanField(
        default=False,
        editable=True,
    )
