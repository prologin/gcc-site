from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_("Utilisateur"),
        on_delete=models.CASCADE,
        related_name="profiles",
    )

    # Participant

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

    # Address applicant
    street_app = models.CharField(
        max_length=64, verbose_name=_("Nom et numéro de voie")
    )
    complement_app = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Complément d'adressse (si nécessaire)"),
    )
    city_app = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_app = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_app = models.CharField(max_length=32, verbose_name=_("Pays"))

    # Legal Guardian

    first_name_resp = models.CharField(
        max_length=256,
        verbose_name=_("Prénom du responsable légal"),
    )

    last_name_resp = models.CharField(
        max_length=256,
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

    street_resp = models.CharField(
        max_length=64, verbose_name=_("Nom et numéro de voie")
    )
    complement_resp = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Complément d'adressse (si nécessaire)"),
    )
    city_resp = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_resp = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_resp = models.CharField(max_length=32, verbose_name=_("Pays"))

    # School

    school_name = models.CharField(
        max_length=64,
        verbose_name=_("Etablissement scolaire de la participante"),
    )

    street_school = models.CharField(
        max_length=64, verbose_name=_("Nom et numéro de voie")
    )
    complement_school = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Complément d'adressse (si nécessaire)"),
    )
    city_school = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_school = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_school = models.CharField(max_length=32, verbose_name=_("Pays"))

    @property
    def participation_count(self):
        # Use reverse accessor to applications
        return self.applications.count

    def __str__(self) -> str:
        return f"<Profile ({self.first_name} {self.last_name} - {self.user})>"

    @staticmethod
    def get_choices_for_user(user):
        choices = [(None, "-")]
        if not user:
            return choices

        choices.extend(
            [
                (p.id, f"{p.first_name} {p.last_name}")
                for p in user.profiles.all()
            ]
        )

        return choices
