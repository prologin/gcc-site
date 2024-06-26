from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


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

    phone = PhoneNumberField(
        verbose_name=_("Numéro de téléphone de la participante"),
        region="FR",
        blank=True,
    )

    # Address applicant
    street_app = models.CharField(
        max_length=64, verbose_name=_("Nom et numéro de voie")
    )
    complement_app = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Complément d'adressse (facultatif)"),
    )
    city_app = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_app = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_app = CountryField(
        verbose_name=_("Pays"),
    )

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

    phone_resp = PhoneNumberField(
        verbose_name=_("Numéro de téléphone du responsable légal"),
        region="FR",
        blank=True,
    )

    street_resp = models.CharField(
        max_length=64, verbose_name=_("Nom et numéro de voie")
    )
    complement_resp = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_("Complément d'adressse (facultatif)"),
    )
    city_resp = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_resp = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_resp = CountryField(verbose_name=_("Pays"))

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
        verbose_name=_("Complément d'adressse (facultatif)"),
    )
    city_school = models.CharField(max_length=64, verbose_name=_("Ville"))
    zipcode_school = models.CharField(
        max_length=16, verbose_name=_("Code postal")
    )
    country_school = CountryField(verbose_name=_("Pays"))

    def __str__(self) -> str:
        return f"<Profile ({self.first_name} {self.last_name} - {self.user})>"

    @property
    def participation_count(self):
        # Use reverse accessor to applications
        return self.applications.count

    @staticmethod
    def get_choices_for_user(user):
        """
        Return a QuerySet of all the profiles attached to the given user
        """
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


@receiver(pre_delete, sender=Profile)
def _profile_delete(sender, instance, *args, **kwargs):
    """
    Signal hook when a Profile is deleted
    """
    for app in instance.applications.all():
        app.profile = None
        app.force_cancelled()
        app.save()
