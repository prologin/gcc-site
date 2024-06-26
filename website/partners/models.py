import hashlib

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from gccsite.storages import GCCMediaStorage


class PartnerStatus(models.TextChoices):
    PROMOTED = "Promoted", _("Partenaires qui nous soutiennent")
    FUNDING = "Funding", _("Partenaires qui nous financent")
    WELCOMING = "Welcoming", _("Partenaires qui nous accueillent")


# ruff: noqa: DJ012
class Partner(models.Model):
    name = models.CharField(
        verbose_name="Nom",
        max_length=256,
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True,
    )

    website_url = models.URLField(
        verbose_name="URL du site",
        blank=True,
        null=True,
    )

    def upload_to(instance, filename):
        hashval = hashlib.sha1(
            (str(instance.id) + instance.name + filename).encode("utf-8")
        ).hexdigest()
        return "sponsors/{}".format(hashval)

    # Ne pas mettre une image trop grande
    logo = models.FileField(
        verbose_name="Logo",
        upload_to=upload_to,
        storage=GCCMediaStorage,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "gif"])],
    )

    status = models.CharField(
        verbose_name="Statut",
        choices=PartnerStatus.choices,
        max_length=20,
        default="Promoted",
    )

    class Meta:
        verbose_name = _("Partenaire")
        verbose_name_plural = _("Partenaires")

    def __str__(self):
        return self.name
