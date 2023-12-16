from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Profile(models.Model):

    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_("Utilisateur"),
        on_delete=models.CASCADE,
        related_name="profiles",
    )

    first_name = models.CharField(
        verbose_name=_("Prénom"),
        max_length=150,
        null=False,
        blank=False
    )

    last_name = models.CharField(
        verbose_name=_("Nom de famille"),
        max_length=150,
        null=False,
        blank=False,
    )

    birth_date = models.DateField(
        verbose_name=_("Date de naissance"),
        null=False,
        blank=False
    )

    email = models.EmailField(
        verbose_name=_("Adresse email"),
        unique=True,
    )

    phone = models.CharField(
        verbose_name=_("Numéro de téléphone"),
        blank=True,
        max_length=16,
    )

    address = models.JSONField(
        verbose_name=_("Adresse"),
        default=dict
    )

    nb_participations = models.IntegerField(
        verbose_name=_("Nombre"),
        blank=True,
        null=True,
        default=0,
    )

    school = models.JSONField(
        verbose_name=_("Établissement scolaire"),
        default=dict,
        blank=True,
        null=True,
    )