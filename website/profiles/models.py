from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_("Utilisateur"),
        on_delete=models.CASCADE,
        related_name="applications",
    )

    first_name = models.CharField(
        null=False,
        max_length=256,
        verbose_name=_("Prénom de la participante"),
    )

    last_name = models.CharField(
        null=False,
        max_length=256,
        verbose_name=_("Nom de la participante"),
    )

    birth_date = models.DateField(
        null=False,
        verbose_name=_("Date de naissance de la participante"),
    )

    email = models.EmailField(
        null=False, verbose_name=_("Adresse email de la participante")
    )

    phone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Numéro de téléphone de la participante"),
    )

    address = models.JSONField(
        verbose_name=_("Adresse de la participante"), default=dict
    )

    first_name_resp = models.CharField(
        max_length=256,
        default="",
        verbose_name=_("Prénom du responsable légal"),
    )

    last_name_resp = models.CharField(
        max_length=256,
        default="",
        verbose_name=_("Nom du responsable légal"),
    )

    email_resp = models.EmailField(
        default="", verbose_name=_("Adresse email du responable légal")
    )

    phone_resp = models.CharField(
        max_length=16,
        blank=True,
        verbose_name=_("Numéro de téléphone du responsable légal"),
    )

    address_resp = models.JSONField(
        verbose_name=_("Adresse du responsable légal"), default=dict
    )

    school = models.JSONField(
        verbose_name=_("Etablissement scolaire de la participante"),
        default=dict,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"<Profile ({self.first_name} {self.last_name} - {self.user})>"
